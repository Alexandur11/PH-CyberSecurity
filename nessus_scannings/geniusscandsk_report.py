import pandas as pd
import xml.etree.ElementTree as ET
from nessus_scannings.utilities import collect_report, severity_mapping, vulnarability_pie_chart, \
    top_plugins_by_vulnerability_count

tree = ET.parse('reports/geniusscansdk_com_xdljmu.nessus')
root = tree.getroot()
data = collect_report(root)
df = pd.DataFrame(data)

df['severity_label'] = df['severity'].map(severity_mapping)
severity = df['severity_label'].value_counts().sort_index() # Counts severities and sorts them
top_plugins = df['pluginName'].value_counts().head(10) # Counts the plugins and takes the top 10, with the most severities.


def display_geniusscandsk_charts():

    """Displays charts by using Matplotlib"""

    vulnarability_pie_chart(severity)
    top_plugins_by_vulnerability_count(top_plugins)
