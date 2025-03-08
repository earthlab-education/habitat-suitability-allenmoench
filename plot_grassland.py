def plot_grassland(gdf, grasslands_gdf):
    gdf = grasslands_gdf[grasslands_gdf.NATIONALGR=='295523010328']
    gdf.dissolve().hvplot(
        geo=True, tiles='EsriImagery',
        title='Pawnee National Grassland',
        fill_color=None, line_color='black', line_width=1.5,
        frame_width=800
    )