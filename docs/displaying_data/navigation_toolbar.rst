Toolbar
=======

Above the image display, there may be a toolbar with buttons that allow you to easily adjust the appearance of the image. It typically includes 10 buttons, which are:

- **Home**: Reset to the initial state.
- **Back**: Go back to the previous view.
- **Forward**: Go forward to the next view.
- **Pan**: (represented by a four-direction arrow icon). Clicking this button changes the mouse cursor to a four-direction arrow in the plot area. At this point, holding down the left mouse button and dragging moves the view; holding the right mouse button and dragging up or right zooms in, while dragging left or down zooms out. Click this button again to exit pan mode. If you drag the color bar area, it adjusts the color mapping range.
- **Zoom**: Clicking this button changes the mouse cursor to a crosshair in the plot area. Holding down the left mouse button and dragging from the top-left to the bottom-right sets the new view range. Click this button again to exit zoom mode.
- **Configure Subplot Layout**: Clicking this button allows you to adjust the relative sizes of the image panels. If things get messed up, press the leftmost **Home** button to return to the initial state.
- **Adjust Subplot**: Clicking this button brings up a configuration dialog where you can adjust detailed parameters such as color mapping, interpolation algorithm, field of view, and range of values.
- **Save**: Clicking this button allows you to save the currently displayed image as a `.png` or `.jpg` file. Note that the output image includes rendered elements like the color bar and axes, rather than the raw data.
- **Scale Bar**: Clicking this button allows you to adjust the properties of the scale bar.

.. image:: /fig/ViewData.png
   :alt: Adjust Viewing Data

.. tip::
   If fewer than 10 buttons are shown, it may be because the available display space is not wide enough. Try maximizing the software window, hiding the left panel, or adjusting the space allocation between the center and right sections of the page.

.. note::
   If there is enough space, the toolbar will also show the coordinates corresponding to the current mouse position on the right side of the buttons.
