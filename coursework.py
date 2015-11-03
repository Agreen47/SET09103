//Alex Green

from flask import Flask, redirect, url_for, abort, render_template
app = Flask(__name__)

@app.route("/artists")
def artists():
  names = ['Bon jovi', 'Cains Offering', 'Dead by April', 'Hammerfall', 'Nightwish', 'Queen',' Skillet', 'The Unguided', 'Two Steps from Hell', 'Within Tempation']
  return render_template('loops.html', names=names)

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  "Couldn't find the page you requested.", 404

@app.route('/artists/bon jovi')
def album1():
  names = ['Bounce', 'Crush']
  return render_template('loops.html', names=names)

@app.route('/artists/bon jovi/bounce')
def tracklist1():
  names = ['Undivided', 'Everyday', 'The Distance', 'Joey', 'Misunderstood', 'All About Lovin You', 'Hook Me Up', 'Right Side of Wrong', 'Love me Back to Life', 'You Had Me from Hello', 'Bounce', 'Open All Night', 'No Regrets', 'Postcards from the Wasteland']
  return render_template('loops.html', names=names)

@app.route('/artists/bon jovi/crush')
def tracklist2():
  names = ['Its My Life', 'Say It Isnt So', 'Thank You for Loving Me', 'Two Story Town', 'Next 100 years', 'Just Older', 'Mystery Train', 'Save the World', 'Captain Crash & The Beauty Queen From Mars', 'Shes a Mystery', 'I Got the Girl', 'One Wild Night', 'I Could Make a Living Out of Lovin You', 'Neurotica']
  return render_template('loops.html', names=names)

@app.route('/artists/cains offering')
def album2():
  names = ['Gather the Faithful', 'Stormcrow']
  return render_template('loops.html', names=names)

@app.route('/artists/cains offering/gather the faithful')
def tracklist3():
  names = ['My Queen of Winter', 'More Than Friends', 'Oceans of Regret', 'Into the Blue', 'Dawn of Solace', 'Thorn in My Side', 'Morpheus in a Masquerade', 'Stolen Waters', 'Tale Untold', 'Elegantly Broken']
  return render_template('loops.html', names=names)

@app.route('/artists/cains offering/stormcrow')
def tracklist4():
  names = ['Stormcrow', 'The Best of Times', 'A Night to Forget', 'I Will Build You a Rome', 'Too Tired to Run', 'Constellation of Tears', 'Antemortem', 'My Heart Beats for No One', 'I Am Legion', 'Rising Sun', 'On the Shore', 'Child Of The Wild']
  return render_template('loops.html', names=names)

@app.route('/artists/dead by april')
def album3():
  names = ['Dead by April', 'Incomparable', 'Let the World Know']
  return render_template('loops.html', names=names)

@app.route('/artists/hammerfall')
def album4():
  names = ['Glory to the Brave', 'Renegade', 'No Sacrifice, No Victory']
  return render_template('loops.html', names=names)

@app.route('/artists/nightwish')
def album5():
  names = ['Wishmaster', 'Imaginaerum', 'Endless Forms Most Beautiful', 'Once']
  return render_template('loops.html', names=names)


@app.route('/artists/queen')
def album6():
  names = ['Flash Gordon', 'Hot Space', 'Greatest Hits']
  return render_template('loops.html', names=names)


@app.route('/artists/skillet')
def album7():
  names = ['Collide', 'Comatose', 'Awake']
  return render_template('loops.html', names=names)

@app.route('/artists/the unguided')
def album8():
  names = ['Hell Frost', 'Nightmareland', 'InvaZion', 'Fragile Immortality']
  return render_template('loops.html', names=names)

@app.route('/artists/two steps from hell')
def album9():
  names = ['Invincible', 'Illusions', 'Archangel', 'SkyWorld']
  return render_template('loops.html', names=names)

@app.route('/artists/within temptations')
def album10():
  names = ['The heart of Everything', 'The Unforgiving', 'Hydra']
  return render_template('loops.html', names=names)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
