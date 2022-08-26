from flask import Flask, redirect, render_template, request, flash, send_file, url_for
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zHyouxw7ztlfgkUV6RfLYY4pifWvT8CD'


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('youtube_url')

        if url.startswith('https://www.youtube.com/watch?v='):
            yt = YouTube(url,
                         on_complete_callback=complete_callback(),
                         )

            thumnail = yt.thumbnail_url
            name = yt.title


            # stream = yt.streams.get_audio_only()
            # audio = stream.download()

            return render_template('/done.html',thumnail=thumnail,name=name)

            # return send_file(audio,
            #                  as_attachment=True,
            #                  mimetype='audio/mp3')


        else:
            flash("Invalid youtube URL", category='error')
            return redirect('/')

    return render_template('/base.html')


def complete_callback():
    return flash("Successfully downloaded", category='success')
