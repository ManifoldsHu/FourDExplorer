Pixel Histogram Filter Method
=============================

If, on the opened page, you click the **Select Window Filter** tab on the top right, you can choose to use the pixel histogram filtering method. The histogram of the currently displayed diffraction image will appear in the center. By setting the minimum and maximum limits for the filter window, you can ensure that the pixel values outside the window are filtered out. The filtering rules are as follows:

- Pixels with values greater than the maximum limit will be set to the maximum limit value.
- Pixels with values less than the minimum limit will be set to 0.

By checking the **Apply Minimum Limit Window** or **Apply Maximum Limit Window** checkboxes, you can display the filtered result in the center of the page. In most cases, to remove background noise (especially noise caused by X-rays), it is enough to set only the minimum limit.

Once the filtering is complete, click the red ``Start Background Subtraction`` button at the bottom of the page to open a dialog where you can set the output path for the resulting dataset.
