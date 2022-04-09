import numpy as np

def haversine(nearest_points):
    """Defines a basic Haversine distance formula."""
    lat1 = nearest_points[0].coords.xy[1][0]
    lon1 = nearest_points[0].coords.xy[0][0]
    lat2 = nearest_points[1].coords.xy[1][0]
    lon2 = nearest_points[1].coords.xy[0][0]

    miles = 3959
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    total_miles = miles * c
    # return feet
    return total_miles * 5280