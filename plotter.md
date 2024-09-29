# Installing deps

1. Install Python (go into advanced and choose the proper options)
2. Install pipx:
   1. `python3 -m pip install --user pipx`
   2. `python3 -m pipx ensurepath`
3. Install vsketch: `pipx install vsketch`

# Generating an SVG

1. Download the examples from here: [https://github.com/abey79/vsketch]
2. Test everything out: `vsk run examples/schotter`
3. Save a copy of the example: `vsk save examples/schotter`
4. Make your own project: `vsk init my_project`
   1. Open in IDLE (or your favorite code editor)
   2. Uncomment lines to make a circle
   3. Change size to `vsk.size("10cm","10cm")`
5. Play with examples, modify them, and look at the docs:
   1. [https://vsketch.readthedocs.io/en/latest/overview.html]
   2. [https://vsketch.readthedocs.io/en/latest/autoapi/vsketch/index.html]
6. Example:
   1. Change the `param` to `degrees` and set to `4`
   2. Add this code

```
	  for i in range(0, 360, self.degrees):
	      with vsk.pushMatrix():
		      vsk.rotate(i, degrees=True)
			  vsk.rect(-2, -2, 2, 2)
```

7. Show Joe's example as well: [https://github.com/allhandsactive/hellojoe]

# Plotting

1. Convert to gcode: [https://sameer.github.io/svg2gcode/]
   1. (default) tolerance: .002
   2. feedrate 5000
   3. (default) originX: 0
   4. (default) originy: 0
   5. (default) do not enable circular interpolation
   6. (default) 96 DPI
   7. Tool On Sequence:
```
      ; tool on
      g0z0
```
   8. Tool Off sequence:
```
      ;
      g0z2
```
   9. Program end sequence: `g0 x0y0`
   10. (default)everything at the bottom unchecked
2. Using the plotter
   1. Open the web interface with a browser. Go to [yourplotter.local]
   2. Try jogging the plotter
   3. Try homing the plotter
   4. Adjust z to 2. Insert a pen so it's just above the paper
   5. Upload a file using the upload button
   6. Tape down paper
   7. Press play button next to downloaded file
