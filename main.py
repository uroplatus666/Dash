import plotly.express as px
from dash import Dash, dcc, html, Input, Output,callback
import pandas as pd
import plotly.graph_objects as go

rosgran=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/StreamLit/master/rosgran.csv')
all_df_copy=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/all_df_copy.csv')
all_df_copy_na=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/all_df_copy_na.csv')
people_zero =pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/people_zero.csv')
places_copy=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/places_copy.csv')
push=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/StreamLit/master/push.csv')
controls_else=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/controls_else.csv')
places_count=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/StreamLit/master/places_count.csv')
rosgran_count=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/rosgran_count.csv')
country_else=pd.read_csv('https://raw.githubusercontent.com/uroplatus666/Dash_StreamLit/master/country_else.csv')

# Initialize app

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(['Распределение пропускных пунктов (по Федеральным округам)',
                  'Распределение пропускных пунктов (по участкам)',
                  'Функционирование пропускных пунктов (по Федеральным округам)',
                  'Функционирование пропускных пунктов (по участкам)',
                  'Пропускные пункты с нулевым фактическим количеством пересечений (по Федеральным округам)',
                  'Пропускные пункты с нулевым фактическим количеством пересечений (по участкам)',
                  'Сумма пересечений пропускных пунктов (по Федеральным округам)',
                  'Усредненное количество пересечений пропускных пунктов (по Федеральным округам)',
                  'Сумма пересечений пропускных пунктов (по участкам)',
                  'Усредненное количество пересечений пропускных пунктов (по участкам)',
                  'Перегруженные пункты пропуска (по Федеральным округам)',
                  'Перегруженные пункты пропуска (по участкам)',
                  'Процент наличия контроля определенного типа на пропускных пунктах (по Федеральным округам)',
                  'Процент наличия контроля определенного типа на пропускных пунктах (по участкам)',
                  'Классификация пропускных пунктов по статусу (по Федеральным округам)',
                  'Классификация пропускных пунктов по статусу (по участкам)'],
                 'Распределение пропускных пунктов (по Федеральным округам)',
                 id='demo-dropdown'),
    dcc.Graph(figure={}, id='dd-output-container')
])


@callback(
    Output('dd-output-container', 'figure'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    if value == 'Распределение пропускных пунктов (по Федеральным округам)':
        fig = go.Figure(data=go.Heatmap(x=rosgran_count['Вид'],
                                        y=rosgran_count['Федеральный округ'],
                                        z=rosgran_count['Количество ПП'],
                                        colorscale="aggrnyl",
                                        text=rosgran_count['Количество ПП'],
                                        colorbar=dict(title='<b>Количество пропускных пунктов</b>')))
        fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
        fig.update_yaxes(title_text='<b>Федеральный округ</b>')

        hover_template = '<b>Федеральный округ</b>: %{y}<br>' + \
                         '<b>Вид пропускного пункта</b>: %{x}<br>' + \
                         '<b>Количество пропускных пунктов</b>: %{z}<extra></extra>'

        fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
        fig.update_layout(height=600, width=1000)
        fig.update_layout(
            title={
                'text': "<b>Распределение пропускных пунктов</b>",
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Распределение пропускных пунктов (по участкам)':
        fig = go.Figure(data=go.Heatmap(x=places_count['Вид'],
                                        y=places_count['Сопредельное государство'],
                                        z=places_count['Количество ПП'],
                                        colorscale='RdGy',
                                        text=places_count['Количество ПП'],
                                        colorbar=dict(title='<b>Количество пропускных пунктов</b>')))

        fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
        fig.update_yaxes(title_text='<b>Сопредельное государство</b>')

        hover_template = '<b>Сопредельное государство</b>: %{y}<br>' + \
                         '<b>Вид пропускного пункта</b>: %{x}<br>' + \
                         '<b>Количество пропускных пунктов</b>: %{z}<extra></extra>'

        fig.update_traces(hovertemplate=hover_template, hoverongaps=False)
        fig.update_layout(height=700, width=1100)
        fig.update_layout(
            title={
                'text': "<b>Распределение пропускных пунктов</b>",
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Функционирование пропускных пунктов (по Федеральным округам)':
        fig=px.histogram(rosgran,y='Федеральный округ',
                         animation_frame="Функционирует/не функционирует",
                         color='Вид',title='<b>Функционирование пропускных пунктов</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=600)
        fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
        fig.update_yaxes(title_text='<b>Федеральный округ</b>')
        hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                         '<b>Федеральный округ</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Функционирование пропускных пунктов</b>",
                'y': 0.94,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Функционирование пропускных пунктов (по участкам)':
        fig=px.histogram(places_copy[(places_copy['Категория']=='Число людей')&
                                     (places_copy['Год']==2022)], y='Сопредельное государство',
                         animation_frame="Функционирует/не функционирует",
                         color='Вид',title='<b>Функционирование пропускных пунктов</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=600)
        fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
        fig.update_yaxes(title_text='<b>Сопредельное государство</b>')
        hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Функционирование пропускных пунктов</b>",
                'y': 0.94,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Пропускные пункты с нулевым фактическим количеством пересечений (по Федеральным округам)':
        fig = px.histogram(people_zero, x="Федеральный округ",
                           animation_frame="Год", color='Вид',
                           facet_col='Функционирует/не функционирует',
                           facet_row='Установлен / закрыт',
                           title='<b>Пропускные пункты с нулевым фактическим количеством пересечений</b>',
                           labels=dict(Вид='<b>Вид пропускного пункта</b>'),
                           height=600)
        fig.update_xaxes(title_text='<b>Федеральный округ</b>')
        fig.update_yaxes(col=1, title_text='<b>Количество пропускных пунктов</b>')
        fig.update_yaxes(col=2, title_text='')
        hover_template = '<b>Количество пропускных пунктов</b>: %{y}<br>' + \
                         '<b>Федеральный округ</b>: %{x}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_yaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Пропускные пункты с нулевым фактическим количеством пересечений</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Пропускные пункты с нулевым фактическим количеством пересечений (по участкам)':
        fig=px.histogram(places_copy[(places_copy['Категория']=='Число людей')&
                                     (places_copy['Количество']==0)],
                         y="Сопредельное государство", animation_frame="Год",
                         color='Вид',facet_row='Функционирует/не функционирует',
                         title='<b>Пропускные пункты с нулевым фактическим потоком людей</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>'), height=800)
        fig.update_xaxes(row=1,title_text='<b>Количество пропускных пунктов</b>')
        fig.update_xaxes(row=2,title_text=None)
        fig.update_yaxes(title_text='<b>Сопредельное государство</b>')
        hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Пропускные пункты с нулевым фактическим количеством пересечений</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

    elif value == 'Сумма пересечений пропускных пунктов (по Федеральным округам)':
        fig=px.histogram(all_df_copy, x="Количество", y="Федеральный округ",
                         animation_frame="Категория",facet_col='Год',
                         orientation='h',facet_col_wrap=2,color="Вид",
                         title='<b>Сумма пересечений пропускных пунктов в 2017-2022 гг.</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>'),height=1000)
        fig.update_yaxes(col=1,title_text='<b>Федеральный округ</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Сумма потоков</b>')
        hover_template = '<b>Сумма пересечений</b>: %{x}<br>' + \
                         '<b>Федеральный округ</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Сумма пересечений пропускных пунктов в 2017-2022 гг.</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Усредненное количество пересечений пропускных пунктов (по Федеральным округам)':
        fig=px.histogram(all_df_copy, x="Количество",
                         y="Федеральный округ", animation_frame="Категория",
                         facet_col='Год',orientation='h',histfunc='avg',
                         facet_col_wrap=2,color="Вид",
                         title='<b>Усредненное количество пересечений пропускных пунктов в 2017-2022 гг.</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>',value=''),height=1000)
        fig.update_yaxes(col=1,title_text='<b>Федеральный округ</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=3,title_text=None)
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Усредненное количество пересечений</b>')
        hover_template = '<b>Усредненное количество пересечений</b>: %{x}<br>' + \
                         '<b>Федеральный округ</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Усредненное количество пересечений пропускных пунктов в 2017-2022 гг.</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Сумма пересечений пропускных пунктов (по участкам)':
        fig=px.histogram(places_copy, x="Количество", y="Сопредельное государство",
                         animation_frame="Категория",facet_col='Год',
                         orientation='h',facet_col_wrap=2,color="Вид",
                         title='<b>Сумма пересечений пропускных пунктов в 2017-2022 гг.</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>'),height=1500)
        fig.update_yaxes(col=1,title_text='<b>Сопредельное государство</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=3,title_text=None)
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Сумма пересечений</b>')
        hover_template = '<b>Сумма пересечений</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Сумма пересечений пропускных пунктов в 2017-2022 гг.</b>",
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Усредненное количество пересечений пропускных пунктов (по участкам)':
        fig=px.histogram(places_copy, x="Количество",
                         y="Сопредельное государство",
                         animation_frame="Категория",
                         facet_col='Год',facet_col_wrap=2,
                         orientation='h', histfunc='avg',color="Вид",
                         title='<b>Усредненное количество пересечений пропускных пунктов в 2017-2022 гг.</b>',
                         labels=dict(Вид='<b>Вид пропускного пункта</b>', value=''),height=1500)
        fig.update_yaxes(col=1,title_text='<b>Сопредельное государство</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=3,title_text=None)
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Усредненное количество пересечений</b>')
        hover_template = '<b>Усредненное количество пересечений</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}<br>'
        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Усредненное количество пересечений пропускных пунктов в 2017-2022 гг.</b>",
                'y': 0.97,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Перегруженные пункты пропуска (по Федеральным округам)':
        fig=px.bar(all_df_copy_na,
                   x="Количество (Факт/Паспорт)", y="Федеральный округ",
                   animation_frame="Категория", facet_col='Год',
                   hover_name='Наименование пункта пропуска',
                   facet_col_wrap=2,color="Вид",
                   title='<b>Перегруженные пункты пропуска в 2017-2022 гг.</b>',
                   labels=dict(Вид='<b>Вид пропускного пункта</b>',value=''),height=1000)
        fig.update_yaxes(col=1,title_text='<b>Федеральный округ</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=3,title_text=None)
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Отношение фактического потока к паспортному</b>')
        hover_template = '<b>Наименование пункта пропуска</b>: %{hovertext}<br>' + \
                         '<b>Отношение фактического потока к паспортному</b>: %{x}<br>' + \
                         '<b>Федеральный округ</b>: %{y}'

        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Перегруженные пункты пропуска в 2017-2022 гг.</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Перегруженные пункты пропуска (по участкам)':
        fig=px.bar(push[(push['Количество (Факт/Паспорт)']>1)&(push['Год']!=2020)],
                   x="Количество (Факт/Паспорт)", y="Сопредельное государство",
                   animation_frame="Категория", facet_col='Год',
                   hover_name='Наименование пункта пропуска',
                   facet_col_wrap=2,color="Вид",
                   title='<b>Перегруженные пункты пропуска в 2017-2022 гг.</b>',
                   labels=dict(Вид='<b>Вид пропускного пункта</b>',value=''),height=1300)
        fig.update_yaxes(col=1,title_text='<b>Сопредельное государство</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(row=3, title_text=None)
        fig.update_xaxes(row=2, title_text=None)
        fig.update_xaxes(row=1, title_text='<b>Отношение фактического потока к паспортному</b>')
        hover_template = '<b>Наименование пункта пропуска</b>: %{hovertext}<br>' + \
                         '<b>Отношение фактического потока к паспортному</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}'

        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Перегруженные пункты пропуска в 2017-2022 гг.</b>",
                'y': 0.96,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Процент наличия контроля определенного типа на пропускных пунктах (по Федеральным округам)':

        fig = go.Figure(data=go.Heatmap(z=controls_else['Процент контроля'],
                                        x=controls_else['Вид'],
                                        y=controls_else['Федеральный округ'],
                                        colorscale='RdBu',
                                        colorbar=dict(title='<b>Процент контроля</b>'),
                                        text=controls_else['Процент контроля'],
                                        customdata=controls_else[['Федеральный округ', 'Вид', 'Процент контроля']])
                        )

        fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
        fig.update_yaxes(title_text='<b>Федеральный округ</b>')

        hover_template = '<b>Федеральный округ</b>: %{customdata[0]}<br>' + \
                         '<b>Вид пропускного пункта</b>: %{customdata[1]}<br>' + \
                         '<b>Процент контроля</b>: %{customdata[2]}%<extra></extra>'

        fig.update_traces(hovertemplate=hover_template, hoverongaps=False)

        # Добавление слайдера для колонки 'Тип контроля'
        steps = []
        for value in controls_else['Тип контроля'].unique():
            visible = controls_else['Тип контроля'] == value
            z_values = controls_else.loc[visible, 'Процент контроля'].values
            step = dict(method='restyle',
                        args=[{'z': [z_values]}],
                        label=value)
            steps.append(step)

        sliders = [dict(steps=steps,
                        active=0,
                        currentvalue={'prefix': 'Тип контроля: '})]

        fig.update_layout(sliders=sliders,height=600,width=1000)
        fig.update_layout(
            title={
                'text': "<b>Процент наличия контроля определенного типа на пропускных пунктах</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Процент наличия контроля определенного типа на пропускных пунктах (по участкам)':

        fig = go.Figure(data=go.Heatmap(z=country_else['Процент контроля'],
                                        x=country_else['Вид'],
                                        y=country_else['Сопредельное государство'],
                                        colorscale='RdBu',
                                        colorbar=dict(title='<b>Процент контроля</b>'),
                                        text=country_else['Процент контроля'],
                                        customdata=country_else[['Сопредельное государство', 'Вид', 'Процент контроля']])
                        )

        fig.update_xaxes(title_text="<b>Вид пропускного пункта</b>")
        fig.update_yaxes(title_text='<b>Сопредельное государство</b>')

        hover_template = '<b>Сопредельное государство</b>: %{customdata[0]}<br>' + \
                         '<b>Вид пропускного пункта</b>: %{customdata[1]}<br>' + \
                         '<b>Процент контроля</b>: %{customdata[2]}%<extra></extra>'

        fig.update_traces(hovertemplate=hover_template, hoverongaps=False)

        # Добавление слайдера для колонки 'Тип контроля'
        steps = []
        for value in country_else['Тип контроля'].unique():
            visible = country_else['Тип контроля'] == value
            z_values = country_else.loc[visible, 'Процент контроля'].values
            step = dict(method='restyle',
                        args=[{'z': [z_values]}],
                        label=value)
            steps.append(step)

        sliders = [dict(steps=steps,
                        active=0,
                        currentvalue={'prefix': 'Тип контроля: '})]

        fig.update_layout(sliders=sliders,height=600,width=1300)
        fig.update_layout(
            title={
                'text': "<b>Процент наличия контроля определенного типа на пропускных пунктах</b>",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})
    elif value == 'Классификация пропускных пунктов по статусу (по Федеральным округам)':
        fig = px.histogram(rosgran, y="Федеральный округ", color='Вид',
                           facet_col='Классификация по статусу',
                           title='<b>Классификация пропускных пунктов по статусу</b>', height=600)
        fig.update_layout(legend=dict(title="<b>Вид пропускного пункта</b>"))
        fig.update_yaxes(col=1,title_text='<b>Федеральный округ</b>')
        fig.update_yaxes(col=2,title_text=None)
        fig.update_xaxes(title_text='<b>Количество пропускных пунктов</b>')
        hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                         '<b>Федеральный округ</b>: %{y}<br>'

        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Классификация пропускных пунктов по статусу</b>",
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

    elif value == 'Классификация пропускных пунктов по статусу (по участкам)':
        places=rosgran[(rosgran['Сопредельное государство']!='не применимо')&
                       (rosgran['Сопредельное государство']!='не применимо (ДНР)')&
                       (rosgran['Сопредельное государство']!='не применимо (ЛНР)')&
                       (rosgran['Сопредельное государство']!='не применимо (Херсонская обл.)')]
        fig = px.histogram(places, y="Сопредельное государство",
                           color='Вид', facet_row='Классификация по статусу',
                           hover_name='Классификация по статусу',
                           title='<b>Классификация пропускных пунктов по статусу</b>', height=800)
        fig.update_layout(legend=dict(title="<b>Вид пропускного пункта</b>"))
        fig.update_xaxes(row=2,title_text=None)
        fig.update_xaxes(row=1,title_text='<b>Количество пропускных пунктов</b>')
        fig.update_yaxes(col=1,title_text='<b>Сопредельное государство</b>')
        fig.update_yaxes(col=2,title_text=None)
        hover_template = '<b>Количество пропускных пунктов</b>: %{x}<br>' + \
                         '<b>Сопредельное государство</b>: %{y}<br>'

        fig.update_traces(hovertemplate=hover_template)
        fig.update_xaxes(showspikes=True, spikemode='across')
        fig.update_layout(
            title={
                'text': "<b>Классификация пропускных пунктов по статусу</b>",
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'})

    return fig


if __name__ == '__main__':
    app.run_server(port=8567)

