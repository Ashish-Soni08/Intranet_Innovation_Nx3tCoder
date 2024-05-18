# Intranet Innovation: Empowering staff for enhanced citizen services

The [Project](https://n3xtcoder.org/intranet-innovation-empowering-staff-for-enhanced-citizen-services) is organised by the City of Moers and [N3XTCODER](https://n3xtcoder.org/).

## Description

As the administration of the City of Moers seeks to meet the evolving needs of its approximately 104,000 residents, the municipal intranet emerges as a pivotal platform for information dissemination and management. Improving the intranet is essential for enhancing the productivity and satisfaction of municipal employees, which in turn will lead to faster, more efficient, and effective services for the citizens of Moers. The challenge is to transform the municipal intranet into a more user-friendly, interactive, and intelligent platform that excels in understanding and generating answers, thereby improving the administration's knowledge base and search capabilities.

- **Goal:** Improve municipal intranet search experience
- **Objective:** Optimise the intranet search capabilities, leading to faster and more precise information retrieval for increased productivity and enhanced value of the intranet as a central communication medium to optmize the performance and satisfaction of administrative staff.
- **Metric:** Projected acceptance rate of search results.

### Impacted People

1. **780** Municipal Workers
2. **106241** citizens in the city of Moers
3. More than **800** sections published in the city intranet

## Environment Setup

```bash
# python version -> 3.10.13
python -V 

# create a environment named -> google-ai
python -m venv intranet-ai

# activate the environment
source intranet-ai/bin/activate

# create a Jupyter Notebook kernel
pip install jupyter
pip install ipykernel

# add your virtual environment as a kernel
python -m ipykernel install --user --name=intranet-ai --display-name="Py3.10-intranet-ai"

# verify kernel installation
jupyter kernelspec list

```

### Download Data

```bash

pip install gdown

# download the zip file from the google drive
gdown <Link to the zip file in the google drive >

# unzip Data
unzip v2-20240508T101819Z-001.zip
```

## Synthetic Data Generation Process

This section provides an overview of the data generation process, ensuring the creation of synthetic datasets that mimic original data while protecting sensitive information.

### Synthetic Dataset v2

- **Structure and Contents**:
  - The dataset includes TXT files with contents similar to the original dataset, ensuring sensitive data like city names and personal names are protected.
  - The TXT files maintain a structure akin to the original PDFs or DOCs that inspired the data synthesis.
  - The folder structure mirrors the original dataset, categorizing different topics to facilitate tracking of the generated files' subject matter.

- **Data Generation Prompts**:
  - **General Prompt**:

    ```markdown
    Analyse what the following text content is about and generate a new one covering the same general topic with FICTIONAL data 
    to PROTECT PRIVACY including FAKE NAME of locations, people, phone numbers, budget amounts, dates, among other sensitive 
    data that rather stays ANONYMOUS. Use ENGLISH OR GERMAN language for the new contents. The text must include title, author, issue date and effective date. Make sure contents has a similar length as the original.
    ```

  - **daenni01_dienstleistungsrahmenvertrag**:

    ```markdown
    Analyse what the following text content is about and generate a new one covering the same general topic with FICTIONAL data 
    to PROTECT PRIVACY. USE FAKE NAMES of locations, people, phone numbers, budget amounts, dates, among other sensitive 
    data that rather stays ANONYMOUS. Use ENGLISH OR GERMAN language for the new contents. The text must include title, author, issue date and effective date. Make sure contents has a similar length as the original.
    ```

  - **Enhanced Privacy Prompt**:

    ```markdown
    Analyse what the following text content is about and generate a new one covering the same general topic with FICTIONAL data 
    to PROTECT PRIVACY. USE FAKE NAMES of locations, people, phone numbers, budget amounts, dates, among other sensitive 
    data that rather stays ANONYMOUS. Use ENGLISH OR GERMAN language for the new contents. The text must include title, author, issue date and effective date. Make sure contents has a similar length as the original. DO NOT MENTION MOERS.
    ```

- **Data Quality and Model Analysis Evaluation**:
  - Questions to evaluate the quality of the data and the model's ability to analyze it are included.

- **Q/A Prompt**:
  - **Initial Prompt**:

    ```markdown
    Analyse the following files provided. Then, generate a complex question about the contents and then indicate 
    the user where the answer can be found and mention any relevant section or chapter. Assume the files are hosted 
    online, so please provide a reference link. DO NOT mention the name of the document in the question itself. 
    AVOID the word DOCUMENT in the question.
    ```

  - **Follow-up Prompt**:

    ```markdown
    Analyse again the two files provided. Then, generate a complex question about the contents and then indicate the 
    user where the answer can be found and mention any relevant section or chapter. Assume the files are hosted online, 
    so please provide a reference link. DO NOT mention the name of the document in the question itself. 
    AVOID the word DOCUMENT in the question.
    ```

## Data Understanding

### Quoting Jonathan from the N3XTCODER TEAM

`We have prepared a synthetic dataset based on real documents and structure from a municipal authority. This dataset is simplified to be text-only (no pdfs, docs) and emulates some of the folder structure of the real data. It also includes some evaluation questions within the file eval_questions_v2.txt.`

`Everything in this dataset is fiction, and it obviously has shortcomings with regards to proving that a solution will work on the real data. However we hope it will help in the design of your solutions. If a solution is promising, then further evaluation work using real data from our challenge partner, can be undertaken at the end of the programme.`

#### Data Directory Structure

![Data Directory Structure](images/project_directory_structure.PNG)

The directory contains various department-specific documents provided in `text file format`, such as mayor's office, education, public services, cultural events, finance, internal services, youth, schools and sports, digitalization, and building management, along with information about synthetic dataset and some evaluation questions.

There are **10** departments with **44** documents in English(29) or German(15), as listed below:

| Department                                 | Total Documents | Language                |
|--------------------------------------------|-----------------|-------------------------|
| Büro Bürgermeister                         | 2               | English                 |
| Eigenbetriebsähnliche Einrichtung Bildung  | 9               | English (5), German (4) |
| ENNI Stadt und Service Niederrhein AöR     | 1               | German                  |
| Festival Moers Kultur GmbH                 | 1               | German                  |
| Finanzen                                   | 2               | English                 |
| Interner Service                           | 21              | English(13), German (8) |
| Jugend                                     | 1               | English                 |
| Schule und Sport                           | 1               | English                 |
| Stab Digitalisierung                       | 2               | English                 |
| Zentrales Gebäudemanagement                | 4               | English (3), German (1) |

`Eigenbetriebsähnliche Einrichtung Bildung` has **3** documents in German, namely:

- `bildung_1-01_-_da_ueber_die_einrichtung_einer_zahlstelle_im_gb_musik_der_eb_bildung`
- `bildung_4-02_-_da_ueber_die_einrichtung_einer_einnahmekasse_im_gb_bibliothek_der_eb_bildung`
- `bildung_04-03_-_da_zur_open_library`

- `bildung_3-01_-_da_ueber_die_einrichtung_einer_zahlstelle_und_von_einnahmekassen_im_gb_vhs_der_eb_bildung` contains a significant amount of text in both German and English, with the majority being in English.

`ENNI Stadt und Service Niederrhein AöR` has **1** document in German, namely:

- `daenni01_dienstleistungsrahmenvertrag`

`Festival Moers Kultur GmbH` has **1** document in German, namely:

- `dafestival-moers-kultur-gmbh`

1. `Interner Service` has **8** documents in German, namely:

- `da3.2-02_elektronische_zeiterfassung`
- `Da3.2-05_Personaldaten`
- `da3.2-06_bildschirmarbeitsplaetze`
- `Da3.2-08_Sponsoring (1)`
- `da3.2-18_gefahrstoffe`
- `da3.4-02_telekommunikationsanlage_hipath_4000`
- `da3.5-01_dezentrale_materialbeschaffung`
- `dv_03-21_zinsloses_darlehen_fahrrad`

`Zentrales Gebäudemanagement` has **1** document in German, namely:

- `dazgm-02_energievers`

### Insights on Synthetic Data Generated from Provided Prompts

Although it is clearly mentioned in the **Prompt** to use one of the languages for the new content that is generated -> `Use ENGLISH OR GERMAN language for the new contents`, there are `TXT` files that have both German and English sentences, they are as follows:

- `da01-03` in  `Büro Bürgermeister` has one sentence at the top in `German` and rest of the content is in `English`.
- `bildung_1_-_dv_02` in `Eigenbetriebsähnliche Einrichtung Bildung` has a top-level sentence in `German` and then the rest of the text in `English`.
- `bildung_3-01_-_da_ueber_die_einrichtung_einer_zahlstelle_und_von_einnahmekassen_im_gb_vhs_der_eb_bildung` in `Eigenbetriebsähnliche Einrichtung Bildung` contains a significant amount of text in both `German` and `English`, with the majority being in `English`.
- `bildung_4-02_-_da_ueber_die_einrichtung_einer_einnahmekasse_im_gb_bibliothek_der_eb_bildung` in `Eigenbetriebsähnliche Einrichtung Bildung` has a sentence at the top in `English` and the rest of the text in `German`.
- `dokumentation_epayment` in `Finanzen` has one paragraph at the top in `German` and the remaining text in `English`.
- `da3.3-05_prozessvereinbarung` in `Interner Service` has a sentence at the top in `German` and the rest of the content in `English`.
- `DA3.4-03_IuK` in `Interner Service` has one word at the top in `German` and the rest of the content in `English`.
- `da3.5-04_frankiermaschinen` in `Interner Service` has one paragraph at the top in `German` and the rest of the content in `English`.
- `DaZGM-05-02_Betriebs-und-DA-Baeder` in `Zentrales Gebäudemanagement` has some text in `German` at the beginning of the document.

**Note:** Since the documents were intended to have a single language, we have manually removed certain text to make them monolingual. Text in one language was removed because the other language was present more predominantly.

The original multilingual files are kept separately in the [original_bilingual_files](data/raw/v2_unzipped/originial_bilingual_files) directory, while the modified monolingual files are stored along with the main data:

- `da01-03` file from `Büro Bürgermeister`

    ```markdown
    13 
 
    Eine neue DSFA ist durchzuführen, wenn die Bedingungen der Verarbeitung sich wesentlich 
    ändern. 
    ```

- `bildung_1_-_dv_02` in `Eigenbetriebsähnliche Einrichtung Bildung`
  
  ```markdown
  OberbürgermeisterIn Beigeordnete Beigeordnete
  Bildung 1- DV 02
  ```

- `bildung_3-01_-_da_ueber_die_einrichtung_einer_zahlstelle_und_von_einnahmekassen_im_gb_vhs_der_eb_bildung` in `Eigenbetriebsähnliche Einrichtung Bildung`

    ```markdown
    Aktueller Gutscheinbestand beträgt: Gutschein-Nr. 1: 2: 3: 300: 
    Erhöhung 
    Vom ________ 
    wurden __ 
    Gutscheine mit dem Gutschein-Nr. __ 300 ausgegeben: 
    Handzeichen 
    Verringerung 
    Am 455 haben lfd. Nummern zwi- 
    schen __ und __ eingelesene Gutschein für VA-Nr. __ 
    mit einem Betrag von __ EURO zur Bargeldkasse entnommen: 
    Handzeichen 
    Erhöhung 
    Am __ 
    wurden __ 
    Gutscheine 
    mit dem Gutschein-Nr. __ bis __ eingelesen: 
    Handzeichen 
    Einsatz 
    Am __ 
    haben lfd. Nummern zwi- 
    schen __ und __ für VA-Nr. __ ein-ge-setz-te Gutschen mit einem Be-trag von __ EURO entnommen. Verantwortliche/r:t I verantwortliche/r: t I g Verantwortliche/r 
    Bildung 3/01
    Wie man die Privatsphäre schützt 
    Dienstanweisung zur Einrichtung von Zahlungsdienststellen und -stellen für geringfügige Bargeldzahlungen im Bereich der Volkshochschule (vhs Stadt Gutenberg) der Eigenbetriebsähnlichen Einrichtung Bildung in der Stadt Gutenberg in der Fassung vom 15.04.2016 

    1. Geltungsbereich 
    Diese Dienstanweisung gilt für die folgenden Dienststellen im Bereich der vhs sowie für geringfügige Bargeldzahlungen bis zur Höhe von 300 € pro Einzelfall (Grenze für Geringfügigkeit): 
    1.1 Die Zahlstelle Mehrzweckkasse der Geschäftsstelle Gutenberg (siehe Abschnitt 7.1.1)
    1.2 Zwei Zahlstellen für Einzelveranstaltungen (siehe Abschnitt 7.1.2-4)
    1.2.1 in der vhs-Gebäude Gutenberg
    1.2.2 in der vhs-Gebäude Kamp-Lintfort
    1.2.3 in verschiedenen Veranstaltungsgebäuden in Gutenberg

    2. Grundlagen 
    2.1 Die in Abschnitt 1. angegebenen Zahlstellen sind dem Eigenbetrieb Bildung, Bereich vhs, organisatorisch zugeordnet. Die Dienst- und Fachaufsicht über die Zahlstellen obliegt der Betriebsleitung des Bereichs vhs.
    2.2 Für die Zahlstellen und sonstige Geldzahlungsvorschriften gelten die entsprechenden Vorschriften für die Stadtkasse. 

    3. Aufgaben der Zahlstelle und der Kassen 
    3.1 Die Mehrzweckkasse gemäß Abschnitt 1.1 hat die von der vhs festgelegten Entgelte zu sammeln, die bar bezahlt werden, sowie Einnahmen aus anderen ihr zugewiesenen Aufgaben (z. B. Verkauf von Gutscheinen, Broschüren, Büchern, Kalendern usw.) und entsprechende Bestandsverzeichnisse (siehe auch Abschnitt 6.2). 
    Die beiden Kassen gemäß Abschnitt 1.2 haben ausschließlich die Eintrittsentgelte für Einzelveranstaltungen gemäß der Gebührenordnung der vhs zu kassieren. 
    Vorhandene Beträge von Gutscheinen werden nicht ausbezahlt, sondern mit Stempel und Unterschrift auf dem Original-Gutschein angegeben. Ausländisches Geld, Schecks und andere Zahlungsmittel werden nicht angenommen. 

    4. Verwaltung der Zahlstellen / Verwaltung der Kassen 
    4.1 Die Verwaltung der Zahlstellen/ Kassen des Bereichs vhs wird von der Verwaltungsleitung übernommen. Die Vertretung der Zahlstellenverwaltung wird vom jeweiligen Vertreter im Amt wahrgenommen.
    4.2 Sofern diese Dienstanweisung nichts anderes bestimmt, trifft die Zahlstellenleitung/ Kassenleitung die erforderlichen Anordnungen zur ordnungsgemäßen Verwaltung der Zahlstelle/ Kasse. Änderungen an den in der Dienstanweisung enthaltenen Mustern sind in Zusammenarbeit mit der Kassenüberwachung und dem Rechnungsprüfungsamt von der Zahlstellenleitung zu veranlassen.
    4.3 Die Zahlstellenleitung/ Kassenleitung hat alle erforderlichen Maßnahmen zu treffen, um die äußere und innere Sicherheit der Kasse zu gewährleisten.
    4.4 Die Zahlstellenleitung/ Kassenleitung überprüft insbesondere:
    4.4.1 die Tagesabschlüsse für bar erhaltene Entgelte gemäß Kassenliste im vhs-Verwaltungsprogramm "BASys" sowie alle anderen Einnahmen, die im Kassenbuch (Anlage 1) eingetragen werden,
    4.4.2 die Abrechnungen der Einzelveranstaltungen,
    4.4.3 die ordnungsgemäße Aufbewahrung und Verwaltung des für die Durchführung der Veranstaltungen erforderlichen Bestands an Eintrittskarten und Gutscheinen sowie anderen für den Verkauf angebotenen wertvollen Beständen.
    4.5 Für die Bedienung der Mehrzweckkasse gemäß Abschnitt 1.1 sind Schlüssel für die Bedienung erforderlich, über deren Verbleib die Zahlstellenleitung ein Schlüsselverzeichnis führt.
    Zur mehreren Schlüssel des Tresors wird ebenfalls ein Schlüsselverzeichnis geführt.
    5. Kassenbedienstete / Zahlstellenbedienstete (Kassierer/Kassiererin) 
    5.1 Der Einsatz der Kassenbediensteten/ Zahlstellenbediensteten wird von der Zahlstellenleitung geregelt.
    5.2 Die Kassenbediensteten/ Zahlstellenbediensteten müssen die Vorschriften zur Kassensicherheit besonders sorgfältig beachten. Mängel oder Unregelmäßigkeiten sind der Zahlstellenleitung umgehend zu melden.
    5.3 Im Einzelnen haben die Kassen- und Zahlstellenbediensteten folgende Aufgaben:
    5.3.1 Kassieren der Entgelte gemäß Gebührenordnung
    5.3.2 Kassieren von Einnahmen aus verschiedenen Verkäufen
    5.3.3 Bare Rückerstattungen bei Einzelfällen
    5.3.4 Führung des Kassenbuchs
    5.3.5 Erstellung des Tagesabschlusses
    5.3.6 Verwaltung des Bestands an Eintrittskarten für Einzelveranstaltungen sowie Gutscheinen für vhs-Veranstaltungen
    5.3.7 Führung des Karten- und Gutscheinbestands-Verzeichnisses sowie anderer Bestandsverzeichnisse
    5.3.8 Übergabe der Einnahmen
    5.3.9 Belegführung
    5.4 Die Kassen- und Zahlstellenbediensteten sind neben der Zahlstellenleitung für die ordnungsgemäße Verwaltung der Kasse verantwortlich. Die Verantwortung umfasst den Bargeldbestand, den Kartenbestand, anderen wertvollen Bestand, die Belegverwaltung, die sichere Verwahrung der Kasse und die Übergabe der Einnahmen auf das Konto der Eigenbetriebsähnlichen Einrichtung Bildung, Bereich vhs.
    6. Behandlung von Fehlbeträgen und Überschüssen 
    6.1 Fehlbeträge und Überschüsse werden in Abschnitt 10. "Falsche Buchung (-) Überschuss (+)" bzw. auf dem Abrechnungsbogen für Eintrittsentgelte (Anlage 3) gesondert genannt und erklärt.
    6.2 Im Kassenbuch wird ebenfalls in Abschnitt 10 der Kassenbuchführung auf bare Erstattungen von gemeldeten Bargeld-Einnahmen hingewiesen. Bare Erstattungen dürfen nur im begründeten Einzelfall aus der Kasse entnommen werden, z. B. kein Bankkonto verfügbar. Auszahlungen sind nur gegen Quittung zulässig.
    6.3 Überschüsse werden zusammen mit den Tageseinnahmen eingezahlt.
    6.4 Kassendifferenzen gegenüber des Soll ist von den Kassen- und Zahlstellenbediensteten unverzüglich der Kassenleitung zu melden. Diese muss Unkorrektheiten aufklären. Wenn Unkorrektheiten nicht ermittelt werden können oder wenn Unregelmäßigkeiten festgestellt werden, muss die Geschäftsbereichsleitung der vhs unverzüglich informiert werden und gegebenenfalls vorläufige Maßnahmen ergriffen werden.
    6.5 Kassendifferenzen müssen von den Kassen- und Zahlstellenbediensteten ausgeglichen werden, wenn der Differenz auf Absprache oder grober Fahrlässigkeit beruht.
    7. Bargeldbestand, Übergabe, Abrechnung 
    Die Bargeldkasse hat die folgenden Barbestände (Wechselgeldvorschüsse):
    Cash
    Bank
    Kotionen 
    Kasse Zukunft 
    Bankkarte Zentrale / Andere
    Kasse E
    Computer 
    Zählwerk 
    Spalten 7 + 8 
    verteilen
    Cash
    200 Euro
    50 Euro
    50 Euro
    50 Euro 
    Hierogityffe/bankweh
    zusammenlegen
    Cash
    200 Euro
    50 Euro
    50 Euro
    50 Euro 
    200 Euro
    50 Euro
    50 Euro
    50 Euro 
    Beim operator muss (lt. →

    Die Gesamthöhlen 
    steigt auf bus noch nap 
    Durch die Anwendung aor PC Knoch 
    Die Summe der abzugefindendem 
    Steigt nur nachsteilen po 
    Bedarfjanahmen, soweit die rückaufstellung notwendig ist, edelmannenn zur restriktiven kleidung der Diesser. 
    Die Rechweims 
    Formularkonstrukt auch erfüllbar und für die ablehnenden links enthalten. 
    Die Ergebnisse Dietlesnder als 
    Kassenzielbaum 
    Woche
    /tag 
    zusammen mitb tragen, sofern den Rückstand abgeschloated 
    ```

- `bildung_4-02_-_da_ueber_die_einrichtung_einer_einnahmekasse_im_gb_bibliothek_der_eb_bildung` in `Eigenbetriebsähnliche Einrichtung Bildung`

    ```markdown
    "Protecting Privacy - A Fictional Tale" by Emily Smith, Issue Date: 07/01/2021, Effective Date: 07/15/2021
    ```

- `dokumentation_epayment` in `Finanzen`

    ```markdown
    Die archivierten elektronischen Unterlagen dürfen ausschließlich von der Stadtkasse in der 
    Einführungsphase der Einführung dieses Dokuments aufgerufen werden. Nach erfolgreich 
    durchgeführter Archivierung haben die zuständigen Organisationseinheiten die Verpflichtung 
    die elektronischen Unterlagen analog der Papierform als steuerrelevant zu transportieren und 
    zu archivieren. 
    Durch die durch die Verantwortung wahrende Aufbewahrungspflicht an die zuständige Fach-
    bereichsleitung muss bei einem Wechsel der Dienststelle analog der Papierform eine Über-
    nahme der archivierten Unterlagen durch den Nachfolger/n ermöglicht werden. Eine Archi-
    vierungsbestätigung ist dem Nachfolger zu übergeben. 
    Die Einsicht in die archivierten Unterlagen ist spätestens bis zum Zeitpunkt der Vernichtung 
    der jeweiligen Dateien möglich. Die Vernichtung der elektronischen Unterlagen ist in den 
    Papierunterlagen zu dokumentieren.  
    
    

    Dokumentation zur Regelung von ePayment-Zahlungen bei Bayer 
    (Version 1.0) 
    
    Dokumentation zur Regelung von ePayment-Zahlungen bei Bayer 
    ```

- `da3.3-05_prozessvereinbarung` in `Interner Service`

    ```markdown
    Im Einzelnen liegt derzeit folgende Überschriftengliederung [ohne lfd. Nrn.] vor:
    ```

- `DA3.4-03_IuK` in `Interner Service`

    ```markdown
    Dienstanweisung
    ```

- `da3.5-04_frankiermaschinen` in `Interner Service`

    ```markdown
    Dienst
    ```

- `DaZGM-05-02_Betriebs-und-DA-Baeder` in `Zentrales Gebäudemanagement`

    ```markdown
    Anlagen:
    A
    Belehrung – Beispiel zu Ziffer 5.2 (1)
    B
    Gesetze und Rechtsvorschriften (Übersicht)
    C
    Arbeitsunterlagen
    Betriebs- und Dienstanweisung für das Personal in den Bädern der Stadt XYZ
    ```

Before Choosing an LLM to act on your data, you need to process the data and load it. The ingestion pipeline consists of three main stages:

1. Load the data
2. Transform the data
3. Index and store the data

### Loaders

We used data connectors, also called **Reader** in Llamaindex, specifically the `SimpleDirectoryReader`, which creates documents out of every file in a given directory to ingest the data from the `text files` provided to us and format the data into `Docment` objects. A `Document` is a collection of data(text) and metadata about that data.  

### Tranformations

After the data is loaded, you then need to process and transform your data before putting it into a storage system. These transformations include

- chunking
- extracting metadata
- embedding each chunk

This is necessary to make sure that the data can be retrieved, and used optimally by the LLM.

Transformation input/output are `Node` objects(a `Document` is a subclass of a `Node`).

WHich textsplitter and why?

### Indexing and Embedding

After loading the data, we have a list of Document objects (or a list of Nodes). It's time to build an `Index` over these objects so we can start querying them.

## Key Decisions

1. LLM - `gpt-3.5-tubro`
2. Vector Database - `Qdrant`

Under the hood, the Retrieval-Augmented Generation (RAG) application uses the following components:

- Embedding model: `jina-embeddings-v2-base-de` German-English bilingual embeddings model via [Jina.ai](https://jina.ai/embeddings#apiform)
- Vector database: [Qdrant](https://qdrant.tech/)
- Large Language Model (LLM): `gpt-3.5-turbo` via [OpenAI](https://platform.openai.com/docs/models/gpt-3-5-turbo)
- Orchestration framework: [LlamaIndex](https://www.llamaindex.ai/)
- App framework: [Gradio](https://www.gradio.app/)
