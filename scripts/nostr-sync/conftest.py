"""Gemeinsames Testgeruest.

Die Integrationstests laufen gegen einen echten `nak serve` auf einem freien Port
— kein Mocking. Damit wird dieselbe Strecke durchlaufen, die spaeter in der CI
zaehlt, inklusive der Eigenheiten von `nak` selbst.
"""

import socket
import subprocess
import time

import pytest

import nak


def _free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


def _wait_until_listening(port: int, timeout: float = 5.0) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        with socket.socket() as probe:
            if probe.connect_ex(("127.0.0.1", port)) == 0:
                return
        time.sleep(0.05)
    raise RuntimeError(f"nak serve auf Port {port} wurde nicht bereit")


@pytest.fixture(scope="session")
def local_relay():
    """Ein In-Memory-Relay samt Blossom-Server, nur fuer diesen Testlauf.

    Session-weit, damit die Suite schnell bleibt; die Unabhaengigkeit der Tests
    sichert stattdessen ein eigener Schluessel je Test (`throwaway_key`).
    """
    port = _free_port()
    server = subprocess.Popen(
        ["nak", "serve", "--blossom", "--port", str(port)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        _wait_until_listening(port)
        yield f"ws://127.0.0.1:{port}"
    finally:
        server.terminate()
        server.wait(timeout=5)


@pytest.fixture(scope="session")
def local_blossom(local_relay):
    return local_relay.replace("ws://", "http://")


@pytest.fixture
def throwaway_key() -> str:
    """Ein frischer Schluessel je Test.

    Ohne das saehe ein Test die Events des vorigen, und die Reihenfolge
    entschiede ueber gruen oder rot.
    """
    return nak.generate_key()
