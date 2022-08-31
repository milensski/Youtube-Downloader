from flask import Flask, redirect, render_template, request, flash, send_file
from pytube import YouTube

from io import BytesIO

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

            # stream = yt.streams.get_audio_only()
            # audio = stream.download()

            return render_template('/done.html', thumnail=thumnail, name=name, url=url)

            # return send_file(audio,
            #                  as_attachment=True,
            #                  mimetype='audio/mp3')

        else:
            flash("Invalid URL", category='error')
            return render_template('index.html')

    return render_template('index.html')


def complete_callback():

    return flash("Successfully downloaded", category='success')


@app.route("/download", methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        buffer = BytesIO()
        url = request.form.get('download_url')
        yt = YouTube(url,
                     on_complete_callback= complete_callback()
                     )

        audio = yt.streams.get_audio_only()

        audio.stream_to_buffer(buffer)
        buffer.seek(0)

        return send_file(buffer,
                         as_attachment=True,
                         download_name= f'{yt.title}.mp4',
                         mimetype='audio/mp4',
                         )


if __name__ == "__main__":
    app.run(debug=True)
