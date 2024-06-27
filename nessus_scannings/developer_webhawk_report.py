import pandas as pd
import xml.etree.ElementTree as ET
from nessus_scannings.utilities import collect_report, severity_mapping, vulnarability_pie_chart, \
    top_plugins_by_vulnerability_count


tree = ET.parse('reports/developer_webhawk_com_414zin.nessus')
root = tree.getroot()

data = collect_report(root)
df = pd.DataFrame(data)

df['severity_label'] = df['severity'].map(severity_mapping)
severity_counts = df['severity_label'].value_counts().sort_index()
top_plugins = df['pluginName'].value_counts().head(10)


print(vulnarability_pie_chart(severity_counts)) # Display chart
print(top_plugins_by_vulnerability_count(top_plugins)) # Display chart
