import matplotlib.pyplot as plt
import seaborn as sns

def collect_report(root):
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

def vulnarability_pie_chart(severity_counts):
    plt.figure(figsize=(8, 8))
    severity_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red', 'purple'])
    plt.title('Vulnerabilities by Severity')
    plt.ylabel('')
    return plt.show()


def top_plugins_by_vulnerability_count(top_plugins):
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