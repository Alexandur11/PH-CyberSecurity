import matplotlib.pyplot as plt
import seaborn as sns

def collect_report(root):
    """
        Collects data from an XML file, specifically extracting information from
        'ReportItem' elements within the XML tree.
        Returns:
            A list of dictionaries, each containing details extracted from a 'ReportItem' element.
            Each dictionary in the returned list contains the following keys:
                - 'port': (str) The port number associated with the report item.
                - 'svc_name': (str) The service name associated with the report item.
                - 'protocol': (str) The protocol associated with the report item.
                - 'severity': (int) The severity level of the report item.
                - 'pluginID': (str) The plugin ID associated with the report item.
                - 'pluginName': (str) The name of the plugin associated with the report item.
                - 'description': (str) The description of the report item.
        """

    data = []
    for element in root.findall('.//ReportItem'):
        entry = {
            'port': element.get('port'),
            'svc_name': element.get('svc_name'),
            'protocol': element.get('protocol'),
            'severity': int(element.get('severity')),
            'pluginID': element.get('pluginID'),
            'pluginName': element.find('plugin_name').text,
            'description': element.find('description').text
        }
        data.append(entry)
    return data

def vulnarability_pie_chart(severity):

    """Takes the severity_counts for a report from Nessus
       returns:
                Pie chart with the distribution of the types of severities."""

    plt.figure(figsize=(8, 8))
    severity.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red', 'purple'])
    plt.title('Vulnerabilities by Severity')
    plt.ylabel('')
    return plt.show()


def top_plugins_by_vulnerability_count(top_plugins):

    """Takes the names and counts of all the plugins scanned
        returns:
                Chart displaying the top 10 plugins sorted by their vulnerability. """

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_plugins.values, y=top_plugins.index, palette='viridis')
    plt.title('Top 10 Plugins by Vulnerability Count')
    plt.xlabel('Count')
    plt.ylabel('Plugin Name')
    plt.tight_layout()
    return plt.show()



severity_mapping = {
    0: 'Informational',
    1: 'Low',
    2: 'Medium',
    3: 'High',
    4: 'Critical'
}