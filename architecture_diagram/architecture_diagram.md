             OLD_DATA                                NEW_DATA                          ANALYSIS

   [Temperature Sensor]                    [Temperature Sensor]
                 ↓                                         ↓
              [Ardiuno]                               [Artisan]
                 ↓                                         ↓
    (in `.alog` format)                      (in `.csv` format)
                 ↓                                         ↓
       [Local Computer]                        [Local Computer]
                 ↓                                         ↓
               [NAS]                           [MySQL Database]
                 ↓                                         ↓
       [Local Computer]                                    ↓
                 ↓                                         ↓
       [MySQL Database]                        [MySQL Database]                   [MySQL Database]
                                                                                           ↓
                                                                                [Jupyter Notebook]

## Project Architecture

The Coffee Data Management project is structured as follows:

- **Old Data**:
    - **Temperature Sensor** collects the temperature readings.
    - The data is processed by **Arduino**, and stored in `.alog` format.
    - The data is then transferred to a **Local Computer** and backed up to a **NAS**.
    - After processing, it is imported into the **MySQL Database**.

- **New Data**:
    - **Artisan** collects temperature data and saves it in `.csv` format.
    - The data is stored on a **Local Computer** and directly imported into the **MySQL Database**.

- **Data Analysis**:
    - Data is extracted from the **MySQL Database** for analysis, which is performed using **Jupyter Notebooks**.

All components interact with each other, ensuring that data flows from sensors and devices to the database for analysis and visualization.
