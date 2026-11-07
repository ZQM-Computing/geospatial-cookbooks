# Environmental planning GIS resource guide

This guide supports **preliminary screening**, alternatives analysis, and defensible GIS data preparation. It does not establish legal jurisdiction, site conditions, permit eligibility, regulatory approval, a certified survey, or an engineering/wetland delineation opinion. Validate the source edition, effective date, coverage, geometry, accuracy, and jurisdiction before any client-facing decision.

## US and Florida reference sources

| Planning question | Starting source | Screening caution |
| --- | --- | --- |
| Flood exposure | [FEMA National Flood Hazard Layer](https://www.fema.gov/flood-maps/national-flood-hazard-layer) | Check effective versus preliminary maps, map revisions, datum, and local floodplain rules; not a parcel-specific flood determination |
| Wetlands | [USFWS National Wetlands Inventory](https://www.fws.gov/program/national-wetlands-inventory/wetlands-data) | Inventory classification is not a jurisdictional delineation; field review and responsible-agency determination may be needed |
| Soils and hydric indicators | [USDA NRCS Web Soil Survey](https://websoilsurvey.nrcs.usda.gov/) | Map-unit estimates and component proportions are not site-specific geotechnical or wetland findings |
| Protected species | [USFWS IPaC](https://ipac.ecosphere.fws.gov/) | Species lists are screening inputs, not absence evidence or completed consultation |
| Impaired waters | [EPA How's My Waterway](https://mywaterway.epa.gov/) | Check assessment cycle, waterbody ID, state listings, and applicable standards |
| Surface water and elevation | [USGS The National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) | Resolution, vertical datum, hydrography vintage, and terrain changes matter |
| Land cover | [MRLC National Land Cover Database](https://www.mrlc.gov/) | Classification is modeled and dated; verify recent land disturbance |
| Conservation areas | [USGS Protected Areas Database](https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-overview) | Ownership and protection designation do not by themselves establish development restrictions |
| Environmental facilities | [EPA ECHO](https://echo.epa.gov/) | Regulatory records are not a Phase I ESA or proof of contamination |
| Florida water and environmental datasets | [Florida DEP Open Data](https://geodata.dep.state.fl.us/) | Verify layer owner, publication date, authoritative program, and current permit records |
| Florida land use and planning | [Florida Geographic Data Library](https://www.fgdl.org/) | Statewide compilations may lag county zoning, future land-use maps, and ordinances |
| Local planning controls | County/municipal planning and property-appraiser GIS | Obtain current zoning, future land use, overlays, setbacks, comprehensive plan, and parcel records from the governing authority |

External links are discovery starting points, **not live-verified downloads or guarantees of current data**. Record actual layer URLs, licensing, access dates, and metadata in each project.

## Repeatable preliminary screening workflow

1. **Define the decision:** parcel/site identifier, jurisdiction, proposed use, alternatives, study area, and agreed screening radius. Avoid treating parcel polygons as surveyed boundaries.
2. **Capture provenance:** dataset owner, title, URL, retrieval time (UTC), published/effective date, license, CRS, resolution/scale, update frequency, and known limitations.
3. **Normalize spatial data:** validate geometries, coordinate reference systems, linear units, nulls, duplicates, and topology. Preserve untouched originals.
4. **Screen independently:** intersect candidate footprints with flood zones, wetlands inventory, hydric-soil indicators, protected areas, impaired waters, land cover, and applicable local planning overlays. Do not infer absence from missing features or unavailable layers.
5. **Quantify uncertainty:** report intersected area and percentage with explicit units; separate measured GIS overlap from regulatory setbacks or required buffers; distinguish no intersection, no coverage, and processing failure.
6. **Compare alternatives:** document assumptions, constraints, source confidence, and trade-offs. Avoid an unexplained composite suitability score.
7. **Quality assurance:** verify boundary/CRS assumptions, spot-check geometry and imagery, reconcile feature counts and area totals, and have a reviewer inspect the map and limitations.
8. **Deliver:** an executive screening summary, source register, constraint matrix, reproducible outputs, map with legend/scale/CRS/date, and an escalation list for qualified local specialists.

## Suggested screening matrix

| Topic | GIS result | Evidence | Follow-up |
| --- | --- | --- | --- |
| Flood hazard | Intersects / does not intersect / unknown | FEMA panel or layer version, effective status | Local floodplain administrator |
| Wetland indicators | Inventory overlap / no mapped overlap / unknown | NWI edition, soil indicators, imagery date | Qualified wetland professional and relevant agencies |
| Species | Potential habitat / species screening flag / unknown | IPaC output and date | Ecologist and agency consultation as appropriate |
| Zoning and future land use | Apparent designation / unknown | Local official map and ordinance date | Local planning/zoning staff |
| Water quality | Listed nearby waterbody / unknown | EPA/state assessment cycle | Environmental specialist |
| Contamination | Facility-record proximity / unknown | EPA/state record ID and date | Environmental professional for appropriate due diligence |

**Never** turn an absent GIS feature into a claim that a regulated resource or risk is absent.

## Cookbook implementation map

- [GeoPandas](https://github.com/ZQM-Computing/geopandas-cookbook): geometry validation, overlays, parcel-to-constraint intersections, reason-coded QA, and repeatable screening tables.
- [PostGIS](https://github.com/ZQM-Computing/postgis-cookbook): indexed spatial joins, multi-user screening datasets, auditability, and role-restricted access.
- [QGIS](https://github.com/ZQM-Computing/qgis-cookbook): analyst review, map layouts, manual interpretation, and documented exports; runtime verification may still be pending.
- [GDAL](https://github.com/ZQM-Computing/gdal-cookbook): raster reprojection, resolution/extent management, and source conversion.
- [Earth Engine](https://github.com/ZQM-Computing/earthengine-cookbook): remote-sensing change screening; currently described as planned patterns, not verified operational analyses.
- [STAC](https://github.com/ZQM-Computing/stac-cookbook): discoverable imagery provenance and acquisition metadata.

## Client-ready scope language

**Included:** preliminary desktop GIS screening, mapped constraints, documented datasets and assumptions, QA findings, and recommended follow-up questions.

**Excluded unless separately contracted with qualified professionals:** boundary or topographic survey, wetland jurisdictional delineation, protected-species survey, Phase I/II environmental site assessment, flood certification, engineering design, legal opinion, permit application, and regulatory approval.

Before quoting a project, confirm geographic scope, number of parcels/alternatives, required layers, map deliverables, turnaround, licensing, and whether local professional review is necessary.
