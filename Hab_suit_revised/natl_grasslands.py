# Define info for grasslands download
grasslands_url = (
    "https://data.fs.usda.gov/geodata/edw/edw_resources/"
    "shp/S_USA.NationalGrassland.zip"
)
grasslands_dir = os.path.join(data_dir, 'grasslands')
os.makedirs(grasslands_dir, exist_ok=True)
grasslands_path = os.path.join(grasslands_dir, 'grasslands.shp')

# Only download once
if not os.path.exists (grasslands_path):
    grasslands_gdf = gpd.read_file(grasslands_url)
    grasslands_gdf.to_file(grasslands_path)

# Load from file
grasslands_gdf = gpd.read_file(grasslands_path)

# Check the data
grasslands_gdf.plot()

# Print the full grasslands_gdf. Note the NATIONALGR column (sort by grassland size)
grasslands_gdf.sort_values(by='GIS_ACRES', ascending=True, inplace=True)
grasslands_gdf