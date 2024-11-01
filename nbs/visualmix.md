### Idea
In 2022, I recorded a new song with the same friends with whom I had recorded the Dino Songs CD ten years earlier: "10 chlini Rägetropfe" (10 Little Raindrops). The song has great dynamics and a varied arrangement, making it quite tricky to hear exactly when each instrument comes in or drops out. That’s how I got the idea to make this visible for listeners in a video! During my readings at schools, I like to explain to students how multitrack recording works and then show them the video. Below, I'll briefly explain how I did it.

### Tracks
The song consists of 9 audio tracks: vocals, 3 guitar tracks, bass, accordion, piano, harmonica, and drums. Strictly speaking, the drum track is a so-called group track, which itself is made up of several individual tracks (bass drum, snare, etc.) as well as additional percussion tracks (tambourine, etc.). For simplicity (and because it’s not possible to record them separately with an acoustic drum kit), these have been combined into a single track.

### Track analysis
In the first step, I calculated the volume information (RMS values) from each track, as I’ll need this for the animation later. Here’s what that looks like:
![Tracks and instruments](Raegetropfe_Tracks_Plot.jpg)
The diagram shows the volume of each track over the entire duration of the song, indicating when and how loudly each one is present in the mix. I also assigned an appropriate instrument image to each track (for the vocals: a microphone). For each track, I needed coordinates for where the instrument image should appear. Since I'm using the cover illustration with the cloud and raindrops as the video background, I placed the instruments on individual "raindrops." Instruments that are heard more on the left in stereo/headphones are assigned coordinates for raindrops on the left side. Drums and bass are centered, as is the vocal.

### Generating images

In the next step, I create the images. A video essentially consists of individual images displayed in rapid succession so that the brain perceives them as continuous motion. A typical frame rate is 25, meaning 25 images per second. For the entire song, which is 231 seconds long, I need around 5,800 images. These are "assembled" one by one like a collage, with the size of each instrument at any given moment reflecting its volume—essentially, the "amplitude" shown in the track plot above. Each instrument image has a maximum square size limit so that they don’t overlap too much. For instance, when an image reaches its maximum width, it can still grow in the other dimension (height) until it forms a square. This effect can be seen with the bass guitar, which becomes thicker rather than longer during loud notes.

The 5,800 images are saved sequentially. For example, the 3,000th image, saved as frame_03000.jpg, represents the song position at 2 minutes and 0 seconds (120 seconds), because 120 seconds * 25 frames = the 3,000th image.

![Sample Image from the video](Raegetropfe_sample_image.jpg)

To make all instruments briefly visible at the very start of the song (when the drums are still creating quiet wind and rain sounds), I replaced the images for the first two seconds with a small "instrument shrink" animation.

### Creating the video

In the final step, I simply needed to convert the 5,800 images along with the fully mixed audio track into an MP4 video. The result looks like this: [YouTube](https://www.youtube.com/watch?v=JGrVT1ECq2E).

### Code

Want to know exactly how I did it? You can find the program code here: [GitHub link: VideoGeneratorForMultiTrackAudio](https://github.com/mtln/VideoGeneratorForMultiTrackAudio/blob/main/VideoGenerator.ipynb).

