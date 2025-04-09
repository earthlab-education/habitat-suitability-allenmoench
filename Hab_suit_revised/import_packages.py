
### load packages

### reproducible file paths
import os
from glob import glob
import pathlib

### gbif packages
import pygbif.occurrences as occ
import pygbif.species as species
from getpass import getpass

### packages for unzipping and handling gbif data
import zipfile
import time

### deal with spatial data
import geopandas as gpd
import xrspatial

### deal with other types of data
import numpy as np
import pandas as pd
import xarray as xr
import rioxarray as rxr
import rioxarray.merge as rxrm
import cartopy.crs as ccrs

### indalid geometries
from shapely.geometry import MultiPolygon, Polygon

### visualizing
import holoviews as hv
import hvplot.pandas
import hvplot.xarray
import matplotlib.pyplot as plt

