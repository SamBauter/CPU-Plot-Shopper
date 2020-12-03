import pandas as pd
from matplotlib.figure import Figure
from matplotlib.colors import ListedColormap
import mpld3
from mpld3 import plugins
from .filters import MonitorFilter
from .models import MonitorSpecs


class BaseGraph:
    def __init__(self, priced_qs_object):
        self.priced_qs = priced_qs_object
        self.df = pd.DataFrame(list(self.priced_qs.all().values()))
        self.css = """
    table
    {
      border-collapse: collapse;
    }
    th
    {
      color: #ffffff;
      background-color: #000000;
    }
    td
    {
      background-color: #cccccc;
      color: #000000;
    }
    table, th, td
    {
      font-family:Arial, Helvetica, sans-serif;
      border: 1px solid black;
      text-align: right;
    }
    """

    def get_labels(self):
        label_list_html = []
        for i in range(len(self.df)):
            # creates label fields from second column onward since brand and model provide a name to the label
            label = self.df.iloc[i, 3:].T
            lab_brand = self.df.iloc[i, 1]
            lab_model = self.df.iloc[i, 2]
            label.name = lab_brand + ": " + lab_model
            label_df = label.to_frame()
            label_list_html.append(str(label_df.to_html()))
        return label_list_html

    def get_html_graph(self, x, y, title, x_label, y_label):
        fig = Figure(figsize=[20, 10])
        ax = fig.subplots()
        ax.grid(True, alpha=0.3)
        points = ax.plot(self.df[x], self.df[y], 'bo',
                         markeredgecolor='k', markersize=3, markeredgewidth=1, alpha=.4)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        labels = self.get_labels()
        tooltip = plugins.PointHTMLTooltip(points[0], labels, voffset=10, hoffset=10, css=self.css)
        plugins.connect(fig, tooltip)

        return mpld3.fig_to_html(fig)


class CategoryGraph(BaseGraph):
    def __init__(self, priced_qs, x, y, title, x_label, y_label):
        super().__init__(priced_qs)
        self.x = x
        self.y = y
        self.title = title
        self.x_label = x_label
        self.y_label = y_label

    def get_html_graph(self):
        return super().get_html_graph(self.x, self.y, self.title, self.x_label, self.y_label)


'''class MonitorGraph:
    def __init__(self, priced_qs_object):
        self.priced_qs = priced_qs_object
        self.df = pd.DataFrame(list(self.priced_qs.all().values()))
        self.css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
  color: #000000;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

    def get_labels(self):
        label_list_html = []
        for i in range(len(self.df)):
            # creates label fields from second column onward since brand and model provide a name to the label
            label = self.df.iloc[i, 3:13].T
            lab_brand = self.df.iloc[i, 1]
            lab_model = self.df.iloc[i, 2]
            label.name = lab_brand + ": " + lab_model
            label_df = label.to_frame()
            label_list_html.append(str(label_df.to_html()))
        return label_list_html

    def get_html_graph(self):
        fig, ax = plt.subplots(figsize=[20, 10])
        ax.grid(True, alpha=0.3)
        points = ax.plot(self.df['price'], self.df['size'], 'bo',
                         markeredgecolor='k', markersize=3, markeredgewidth=1, alpha=.4)
        ax.set_xlabel('Price ($)')
        ax.set_ylabel('Monitor Size (inches)')
        ax.set_title('Monitors by Size, Price and Panel Type')
        labels = self.get_labels()
        tooltip = plugins.PointHTMLTooltip(points[0], labels, voffset=10, hoffset=10, css=self.css)
        plugins.connect(fig, tooltip)

        return mpld3.fig_to_html(fig)
        '''
