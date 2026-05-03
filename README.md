# used_car_pricing
## Assignment 11.1
### Berkeley Practical Application Assignment

This repository is organized to separate reusable code, analysis notebooks, raw data, and visual assets.

### Repository structure
- `README.md` — project overview and file structure
- `data/` — raw dataset files
- `images/` — generated plots and visual assets
- `notebooks/` — Jupyter notebooks for data loading, exploratory analysis, and modeling
- `src/` — reusable Python helper code

### Key files
- `src/data_prep.py` — helper functions for loading and cleaning the dataset
- `notebooks/data_loading_cleaning.ipynb` — data loading, inspection, and cleaning steps
- `notebooks/exploratory_data_analysis.ipynb` — exploratory data analysis and visualizations
- `notebooks/used_car_price_analysis.ipynb` — predictive modeling and pricing analysis
- `data/vehicles.csv` — dataset of used car listings

### Findings and recommendations
#### Key findings
- Vehicle age and mileage are the biggest price drivers: newer cars and those with fewer miles consistently sell for higher prices.
- Vehicle brand matters significantly: luxury and performance brands like Ferrari, Tesla, and Porsche sell for much higher prices than economy brands.
- Vehicle condition is critical: cars listed as "like new" or "excellent" sell for much more than "fair" or "salvage" vehicles.
- Diesel and electric vehicles are priced higher than gas cars, indicating customer value for fuel savings and efficiency.

#### Model performance
The best model was Ridge Regression with tuning. RMSE was chosen as the primary metric because it penalizes large pricing errors — ideal for used car dealerships that want to maximize profitability and reduce costly mispricing.  I investigated Lasso but RMSE was higher than Ridge Regression.

#### Recommendations for used car dealerships
- Acquire newer, low-mileage inventory, since these are the clearest indicators of higher resale value.
- Invest in reconditioning vehicles by repairing paint, fixing dents, and detailing cars before posting pictures.
- Build a pricing tool that consumes vehicle features and outputs a competitive listing price.
