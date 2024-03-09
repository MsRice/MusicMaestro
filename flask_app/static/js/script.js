// -- Spotify API Fetching Logic 

function fetchSongsFromSpotifyAPI() {
    // Make API calls using your Python/Flask backend
    // Return an array of song objects with properties:
    //    * artistName
    //    * songTitle
    //    * albumImageUrl
    //    * audioPreviewUrl 
}

// -- Global Variables --
const songData = fetchSongsFromSpotifyAPI();
let currentQuestion = 0;
let correctScore = 0;
let incorrectScore = 0;
const totalQuestions = 10;
let currentSong;

// -- DOM References --
const playButton = document.querySelector('.play-button');
const answerButtons = document.querySelectorAll('.answer-button');
const scoreCorrect = document.getElementById('correct-score');
const scoreIncorrect = document.getElementById('incorrect-score');
const feedback = document.getElementById('feedback');

// -- Event Listeners --
playButton.addEventListener('click', startGame);
answerButtons.forEach(button => button.addEventListener('click', checkAnswer));

// -- Game Functions --
function startGame() {
    // Hide the play button
    playButton.classList.add('hidden');

    // Reset scores (if restarting)
    correctScore = 0;
    incorrectScore = 0;
    updateScoreboard();

    // Start with the first question
    currentQuestion = 0;
    askQuestion();
}

function askQuestion() {
    if (currentQuestion >= totalQuestions) {
        endGame();
        return;
    }
    currentSong = getRandomSong();
    displayQuestion(currentSong);
    playSongPreview(currentSong.audioPreviewUrl);
}

function getRandomSong() {
    const randomIndex = Math.floor(Math.random() * songData.length);
    return songData[randomIndex];
}

function displayQuestion(song) {
    // Generate 3 incorrect choices 
    const allChoices = [song, ...incorrectChoices];
    shuffle(allChoices);
    // Populate answerButtons with choices, including albumImage  
}

function playSongPreview(url) {
    let audio = new Audio(url);
    audio.play();
    // Set a 10-second timeout
    setTimeout(() => {
        audio.pause();
    }, 10000);
}

function checkAnswer(event) {
    const clickedButton = event.target;
    const clickedArtist = clickedButton.querySelector('.artist-name').textContent;
    const clickedSong = clickedButton.querySelector('.song-title').textContent;

    if (clickedArtist === currentSong.artistName && clickedSong === currentSong.songTitle) {
        correctScore++;
        feedback.textContent = "Well Done!";
    } else {
        incorrectScore++;
        feedback.textContent = "Sorry";
    }

    updateScoreboard();
    feedback.classList.remove('hidden'); // Show feedback message

    // Short delay before moving to the next question
    setTimeout(() => {
        feedback.classList.add('hidden');
        currentQuestion++;
        askQuestion();
    }, 1000); // 1 second delay
}

function updateScoreboard() {
    scoreCorrect.textContent = correctScore;
    scoreIncorrect.textContent = incorrectScore;
}

function endGame() {
    // Example: Simple alert, you can make this more elaborate
    alert(`Game Over! You got ${correctScore} out of ${totalQuestions} correct!`);

    // Option to play again:
    playButton.textContent = "Play Again";
    playButton.classList.remove('hidden');
}


function shuffle(array) {
    var currentIndex = array.length, randomIndex;

    // While there remain elements to shuffle...
    while (currentIndex != 0) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex], array[currentIndex]];
    }

    return array;
}
