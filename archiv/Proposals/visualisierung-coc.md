### Proposal: Visualisierung des Beziehungsgeschehens innerhalb der Community of Communities
**Ziel:** Darstellung der Beziehungen und Interaktionen zwischen verschiedenen Communities und ihren Mitgliedern, um Transparenz, Zusammenarbeit und Beteiligung zu fördern.

#### Beschreibung:
Das Beziehungsgeschehen zwischen verschiedenen Communities und ihren Mitgliedern soll durch ein interaktives Netzwerkdiagramm visualisiert werden. Dies hilft, die Vernetzung und Zusammenarbeit innerhalb der Community of Communities sichtbar zu machen und zu fördern. Durch die Visualisierung können Mitglieder sehen, wie sie miteinander verbunden sind, welche Ressourcen und Kompetenzen verfügbar sind und wie sie sich aktiv einbringen können.

#### Vorteile:
- **Transparenz:** Klarer Überblick über die Beziehungen und Interaktionen zwischen den Communities und ihren Mitgliedern.
- **Zusammenarbeit:** Förderung der Zusammenarbeit durch Identifizierung von Schnittstellen und Synergien.
- **Beteiligung:** Erhöhung der Beteiligung durch Sichtbarkeit von Mitmachmöglichkeiten und Aktivitäten.
- **Ressourcenmanagement:** Effizientere Nutzung und Verteilung von Ressourcen und Kompetenzen.

#### Maßnahmen:
1. **Datenerhebung und -strukturierung:**
   - **Benutzerprofile und Communities:** Erhebung von Daten über Mitglieder und Communities, einschließlich Kompetenzen, Ressourcen und Aktivitäten.
   - **Beziehungsdaten:** Erfassung der Beziehungen zwischen Mitgliedern und Communities, z.B. durch benutzerdefinierte Felder in WordPress oder über APIs von anderen CMS.

2. **Technische Umsetzung:**
   - **Integration von D3.js:** Nutzung der D3.js-Bibliothek zur Erstellung eines interaktiven Netzwerkdiagramms, das die Beziehungen visualisiert.
   - **API-Integration:** Abrufen der Daten aus verschiedenen Systemen (WordPress und andere CMS) über REST APIs oder GraphQL.
   - **Dynamische Datenvisualisierung:** Erstellung eines Skripts zur dynamischen Visualisierung der Daten, das regelmäßig aktualisiert wird.

3. **Interaktive Funktionen:**
   - **Zoom und Pan:** Ermögliche es den Nutzern, in das Netzwerkdiagramm hineinzuzoomen und sich darin zu bewegen, um spezifische Beziehungen und Details zu erkunden.
   - **Tooltips und Details:** Anzeige von Tooltips mit zusätzlichen Informationen (z.B. Mitgliedskompetenzen, Community-Ressourcen), wenn der Benutzer über Knoten oder Verbindungen fährt.
   - **Filter und Suchfunktionen:** Integration von Filter- und Suchfunktionen, um bestimmte Beziehungen oder Mitglieder schnell zu finden.

4. **Einbindung und Nutzung:**
   - **Schulung und Einführung:** Bereitstellung von Schulungen und Anleitungen für die Mitglieder, um das Netzwerkdiagramm effektiv zu nutzen.
   - **Feedback und Anpassung:** Regelmäßige Einholung von Feedback der Nutzer zur Optimierung und Verbesserung der Visualisierung.

5. **Beispielhafte Implementierung:**
   - **Datenabruf und -verarbeitung:** Abrufen von Daten aus WordPress und anderen CMS über APIs.
   - **Netzwerkdiagramm mit D3.js:** Beispielhaftes Skript zur Erstellung des Netzwerkdiagramms:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Community Network</title>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style>
        .node {
            stroke: #fff;
            stroke-width: 1.5px;
        }
        .link {
            stroke: #999;
            stroke-opacity: 0.6;
        }
    </style>
</head>
<body>
    <script>
        async function fetchData() {
            const communityResponse = await fetch('https://community.oer/wp-json/wp/v2/community');
            const personResponse = await fetch('https://community.oer/wp-json/wp/v2/person');
            const activityResponse = await fetch('https://community.oer/wp-json/wp/v2/activity');

            const communities = await communityResponse.json();
            const persons = await personResponse.json();
            const activities = await activityResponse.json();

            const nodes = [
                ...communities.map(item => ({
                    id: item.id,
                    name: item.title.rendered,
                    type: 'community'
                })),
                ...persons.map(item => ({
                    id: item.id,
                    name: item.title.rendered,
                    type: 'person'
                }))
            ];

            const links = [];
            communities.forEach(community => {
                const members = community.acf.members || [];
                members.forEach(member => {
                    links.push({
                        source: community.id,
                        target: member.ID // ACF returns related post ID
                    });
                });
            });

            activities.forEach(activity => {
                links.push({
                    source: activity.acf.person.ID, // Beziehung zur Person
                    target: activity.acf.community.ID, // Beziehung zur Community
                    activity: activity.acf.description, // Beschreibung der Aktivität
                    date: activity.acf.date // Datum der Aktivität
                });
            });

            createNetwork(nodes, links);
        }

        function createNetwork(nodes, links) {
            const width = 960;
            const height = 600;

            const svg = d3.select("body").append("svg")
                .attr("width", width)
                .attr("height", height);

            const simulation = d3.forceSimulation(nodes)
                .force("link", d3.forceLink(links).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-400))
                .force("center", d3.forceCenter(width / 2, height / 2));

            const link = svg.append("g")
                .attr("class", "links")
                .selectAll("line")
                .data(links)
                .enter().append("line")
                .attr("class", "link")
                .attr("stroke-width", d => d.activity ? 2 : 1) // Dickere Linien für Aktivitäten
                .on("mouseover", function(event, d) {
                    if (d.activity) {
                        // Tooltip für Aktivitäten anzeigen
                        d3.select(this)
                            .append("title")
                            .text(`${d.activity} am ${d.date}`);
                    }
                });

            const node = svg.append("g")
                .attr("class", "nodes")
                .selectAll("circle")
                .data(nodes)
                .enter().append("circle")
                .attr("class", "node")
                .attr("r", 10)
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended));

            node.append("title")
                .text(d => d.name);

            simulation.on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);
            });

            function dragstarted(event, d) {
                if (!event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

            function dragged(event, d) {
                d.fx = event.x;
                d.fy = event.y;
            }

            function dragended(event, d) {
                if (!event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }
        }

        fetchData();
    </script>
</body>
</html>
```

Um ein Netzwerkdiagramm in D3.js mit Daten aus WordPress zu betreiben, solltest du die folgenden Schritte unternehmen, um die Datenstruktur in WordPress entsprechend aufzubauen:

### Custom Post Types und Custom Fields
1. **Custom Post Types**: Erstelle zwei benutzerdefinierte Beitragstypen (Custom Post Types) für Communities und Personen.
2. **Custom Fields**: Verwende benutzerdefinierte Felder (Custom Fields), um zusätzliche Informationen zu speichern, wie z.B. die Verbindungen zwischen Personen und Communities.

### Beispiel für die Datenstruktur:
#### 1. Custom Post Type für Communities
- **Name**: `community`
- **Felder**:
  - `name` (Titel des Beitrags)
  - `description` (Beschreibung der Community)
  - `members` (Benutzerdefiniertes Feld, das eine Liste von Mitgliedern enthält, die zu dieser Community gehören. Das könnte eine Beziehung zu den Personen-Beiträgen sein.)

#### 2. Custom Post Type für Personen
- **Name**: `person`
- **Felder**:
  - `name` (Titel des Beitrags)
  - `skills` (Liste von Kompetenzen)
  - `communities` (Benutzerdefiniertes Feld, das eine Liste von Communities enthält, zu denen die Person gehört)

### Einrichtung der Custom Post Types
Du kannst diese benutzerdefinierten Beitragstypen in deinem WordPress-Theme oder einem Plugin definieren. Hier ein Beispiel für die functions.php deines Themes:

```php
function create_custom_post_types() {
    // Custom Post Type für Communities
    register_post_type('community',
        array(
            'labels' => array(
                'name' => __('Communities'),
                'singular_name' => __('Community')
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array('title', 'editor', 'custom-fields')
        )
    );

    // Custom Post Type für Personen
    register_post_type('person',
        array(
            'labels' => array(
                'name' => __('Persons'),
                'singular_name' => __('Person')
            ),
            'public' => true,
            'has_archive' => true,
            'supports' => array('title', 'editor', 'custom-fields')
        )
    );
}
add_action('init', 'create_custom_post_types');
```

### Benutzerdefinierte Felder (Custom Fields)
Verwende ein Plugin wie Advanced Custom Fields (ACF), um die benutzerdefinierten Felder zu definieren.

#### Beispiel für die Felder:
- **Community**:
  - Feldgruppe: `Community Details`
    - Feldname: `description` (Beschreibung der Community)
    - Feldname: `members` (Beziehung zu `person`-Beiträgen)
- **Person**:
  - Feldgruppe: `Person Details`
    - Feldname: `skills` (Textfeld für Kompetenzen)
    - Feldname: `communities` (Beziehung zu `community`-Beiträgen)

### Datenabruf und Darstellung
Verwende die WordPress REST API, um diese Daten abzurufen.

#### Beispiel für den Datenabruf:
```js
async function fetchData() {
    const communityResponse = await fetch('https://community.oer/wp-json/wp/v2/community');
    const personResponse = await fetch('https://community.oer/wp-json/wp/v2/person');

    const communities = await communityResponse.json();
    const persons = await personResponse.json();

    const nodes = [
        ...communities.map(item => ({
            id: item.id,
            name: item.title.rendered,
            type: 'community'
        })),
        ...persons.map(item => ({
            id: item.id,
            name: item.title.rendered,
            type: 'person'
        }))
    ];

    const links = [];
    communities.forEach(community => {
        const members = community.acf.members || [];
        members.forEach(member => {
            links.push({
                source: community.id,
                target: member.ID // ACF returns related post ID
            });
        });
    });

    createNetwork(nodes, links);
}
```


Kommentare willkommen ...
