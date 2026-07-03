import plotly.express as px


def line_chart(
    dataframe,
    x,
    y,
    title
):

    fig = px.line(
        dataframe,
        x=x,
        y=y,
        title=title
    )

    return fig


def bar_chart(
    dataframe,
    x,
    y,
    title
):

    fig = px.bar(
        dataframe,
        x=x,
        y=y,
        title=title
    )

    return fig