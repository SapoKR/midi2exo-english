class ExoVideo(dict):
    def __init__(
        self, start=1, end=2, layer=1, group=1, overlay=1, camera=0, video={}, flip=0
    ):
        dict.__init__(
            self,
            {
                "start": start,
                "end": end,
                "layer": layer,
                "group": group,
                "overlay": overlay,
                "camera": camera,
                "sceneSettings": video,
                "effects": [
                    {
                        "_name": "Reversal",
                        "Flip vertical": 0,
                        "Flip horizontal": flip,
                        "Invert luminance": 0,
                        "Hue inversion": 0,
                        "Transparency inversion": 0,
                    },
                    {
                        "_name": "Standard drawing",
                        "X": 0.0,
                        "Y": 0.0,
                        "Z": 0.0,
                        "Zoom%": 100.00,
                        "Clearness": 0.0,
                        "Rotation": 0.00,
                        "blend": 0,
                    },
                ],
            },
        )


class SceneSettings(dict):
    def __init__(self, file, alpha=0, playback=1, vplay=100.0, loop=0):
        dict.__init__(
            self,
            {
                "_name": "Video file",
                "Playback position": playback,
                "vPlay": vplay,
                "Loop playback": loop,
                "Import alpha channel": alpha,
                "file": file,
            },
        )
