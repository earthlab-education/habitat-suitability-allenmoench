# def plot_grassland(gdf, grasslands_gdf):
#     gdf = grasslands_gdf[grasslands_gdf.NATIONALGR=='295523010328']
#     gdf.dissolve().hvplot(
#         geo=True, tiles='EsriImagery',
#         title='Pawnee National Grassland',
#         fill_color=None, line_color='black', line_width=1.5,
#         frame_width=800
#     )

import pandas as pd
import geopandas as gpd
import holoviews as hv

hv.extension('bokeh')

def plot_grassland(grasslands_gdf, nationalgr_code, plot_title):
    """
    Plots a specific grassland area from a GeoDataFrame based on a given NATIONALGR code.

    Args:
        grasslands_gdf (gpd.GeoDataFrame): GeoDataFrame containing grassland data with a 'NATIONALGR' column.
        nationalgr_code (str): The NATIONALGR code of the grassland to plot.
        plot_title (str): The title to be displayed on the plot.

    Returns:
        hv.plotting.plot.Plot: The HoloViews plot of the specified grassland.
    """
    gdf = grasslands_gdf[grasslands_gdf.NATIONALGR == nationalgr_code]
    plot = gdf.dissolve().hvplot(
        geo=True, tiles='EsriImagery',
        title=plot_title,
        fill_color=None, line_color='black', line_width=1.5,
        frame_width=800
    )
    return plot