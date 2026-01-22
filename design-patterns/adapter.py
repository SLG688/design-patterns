from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, filename: str) -> str:
        pass

class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, filename: str) -> str:
        if audio_type == "mp3":
            return f"播放MP3文件: {filename}"
        elif audio_type == "wav":
            return f"播放WAV文件: {filename}"
        else:
            return f"不支持的音频格式: {audio_type}"

class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, filename: str) -> str:
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str) -> str:
        pass

class VLCPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename: str) -> str:
        return f"使用VLC播放: {filename}"
    
    def play_mp4(self, filename: str) -> str:
        return f"使用VLC播放MP4: {filename}"

class MediaAdapter(MediaPlayer):
    def __init__(self, advanced_player: AdvancedMediaPlayer):
        self.advanced_player = advanced_player
    
    def play(self, audio_type: str, filename: str) -> str:
        if audio_type == "vlc":
            return self.advanced_player.play_vlc(filename)
        elif audio_type == "mp4":
            return self.advanced_player.play_mp4(filename)
        else:
            return f"不支持的格式: {audio_type}"

def adapter_demo():
    print("=" * 50)
    print("适配器模式 (Adapter Pattern)")
    print("=" * 50)
    
    player = MediaPlayer()
    
    print("\n使用基本播放器:")
    print(player.play("mp3", "song.mp3"))
    print(player.play("wav", "sound.wav"))
    print(player.play("mp4", "video.mp4"))
    
    print("\n使用适配器:")
    vlc_player = VLCPlayer()
    adapter = MediaAdapter(vlc_player)
    player._adapter = adapter
    
    print(player.play("vlc", "movie.vlc"))
    print(player.play("mp4", "video.mp4"))
    
    print("\n应用场景:")
    print("- 集成第三方库")
    print("- 接口转换")
    print("- 遗留代码兼容")
    print("- 不同系统间通信")

if __name__ == "__main__":
    adapter_demo()
