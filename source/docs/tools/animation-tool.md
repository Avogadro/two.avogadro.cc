(tools-animation-tool)=

# Animation Tool

![The icon of the Animation Tool in light mode.](../../_static/icon_player.svg)

Keyboard shortcut: <kbd>Ctrl</kbd>+<kbd>9</kbd>

## Basic Usage

The animation tool allows you to view a sequence of multiple coordinate sets, whether part of a molecular dynamics trajectory, a geometry optimization, a reaction pathway, or a set of conformers.

![Screenshot of the animation panel](../../_static/animation.png)

The simplest option is to simply click <kbd>Play</kbd> to view the animation. It will loop through repeatedly until you click <kbd>Pause</kbd>.

If you wish to move through the frames one by one, you can use the controls at the top of the panel:

![Screenshot of the animation panel indicating move buttons](../../_static/animate-move.png)

The slider can be used to drag between frames, or you can click the <kbd><</kbd> or <kbd>></kbd> buttons to move backwards (1) or forward (3) one frame at a time.

If you wish to focus only on one part of the trajectory, you can use the Start and End controls, which will limit the range of the animation:

![Screenshot of the animation panel indicating start and end controls](../../_static/animate-start-end.png)

In some cases, an animation may include breaking or forming bonds. In this case, check "Dynamic bonding" for Avogadro to adjust bonds for each frame.

Finally, to speed up or slow down the animation, you can control the Frame rate in frames per second (FPS):

![Screenshot of the animation panel indicating the frame rate control](../../_static/animate-fps.png)

:::{tip}
You can record the entire animation as a GIF or AVI file in Avogadro or save a set of PNG images to convert to an MP4 movie with the [ffmpeg](https://www.ffmpeg.org/) package. The resolution will be identical to the current window.
:::

## See Also

- {ref}`tutorials-viewing-vibrations` – Visualize vibrational modes from calculations
- {ref}`optimize-conformers` – Generate and explore molecular conformers
- {ref}`tools-navigation-tool` – Rotate and zoom the view during playback
