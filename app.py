from io import BytesIO

from flask import Flask, redirect, render_template, request, flash, send_file
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zHyouxw7ztlfgkUV6RfLYY4pifWvT8CD'


@app.route('/')
def home():
    return redirect('index')


@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('youtube_url')

        if url.startswith('https://www.youtube.com/watch?v='):
            yt = YouTube(url)

            thumnail = yt.thumbnail_url
            name = yt.title
            video_and_audio = yt.streams.filter(progressive=True)

            return render_template('/done.html', thumnail=thumnail, name=name, url=url, video_and_audio=video_and_audio)

        else:
            flash("Invalid URL", category='error')
            return render_template('index.html')

    return render_template('index.html')


def complete_callback():
    return flash("Successfully downloaded", category='success')


@app.route("/download", methods=['GET', 'POST'])
def download():
    if request.method == 'POST':

        url = request.form.get('download_url')
        itag = request.form.get('itag')

        buffer = BytesIO()
        yt = YouTube(url,
                     on_complete_callback=complete_callback()
                     )
        if itag == 'Audio':
            audio = yt.streams.get_audio_only()
            audio.stream_to_buffer(buffer)
        else:

            video = yt.streams.get_by_itag(int(itag))

            video.stream_to_buffer(buffer)

        buffer.seek(0)

        return send_file(buffer,
                         as_attachment=True,
                         download_name=f'{yt.title}.mp4',
                         mimetype='video/mp4',
                         )


if __name__ == "__main__":
    app.run(debug=True)
