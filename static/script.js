/* particlesJS.load(@dom-id, @path-json, @callback (optional)); */
particlesJS.load('particles-js', 'static/particles.json', function() {
  console.log('callback - particles.js config loaded');
});

document.addEventListener('DOMContentLoaded', function () {
    // Find the search form and mic button
    const searchForm = document.querySelector('#search-form');
    const micBtn = document.querySelector('#mic-btn');

    // If this script is on a page without these elements, stop to prevent errors.
    if (!searchForm || !micBtn) {
        return;
    }

    const searchInput = searchForm.querySelector('input[name="query"]');

    // Check if the browser supports Speech Recognition
    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        
        // --- CHANGE 1: FASTER RESPONSE ---
        // Set to true to get live, in-progress results
        recognition.interimResults = true; 
        
        recognition.lang = 'en-US';

        // --- CHANGE 2: STOP ON CLICK ---
        // We need a function to handle stopping, so we can add/remove it
        const stopRecognitionOnClick = () => {
            console.log('Page clicked, stopping recognition.');
            recognition.stop();
        };

        // Start recognition when the mic button is clicked
        micBtn.addEventListener('click', () => {
            try {
                recognition.start();
                // Add a listener to the entire document to stop recognition
                document.addEventListener('click', stopRecognitionOnClick);
                // You could also add a visual "listening" class to the mic button here
                // micBtn.classList.add('is-listening');
            } catch (e) {
                console.error('Speech recognition could not be started.', e);
                // Make sure to remove the listener if starting fails
                document.removeEventListener('click', stopRecognitionOnClick);
            }
        });

        // Fired when speech recognition ends (for any reason)
        recognition.onend = () => {
            // ALWAYS remove the click listener when recognition ends
            document.removeEventListener('click', stopRecognitionOnClick);
            // Remove any "listening" class here
            // e.g., micBtn.classList.remove('is-listening');
        };

        // --- UPDATED LOGIC FOR FASTER RESPONSE ---
        // Fired when a result (either interim or final) is received
        recognition.onresult = (event) => {
            let interimTranscript = '';
            let finalTranscript = '';

            // Loop through all results
            for (let i = event.resultIndex; i < event.results.length; ++i) {
                const transcript = event.results[i][0].transcript;
                if (event.results[i].isFinal) {
                    finalTranscript += transcript;
                } else {
                    interimTranscript += transcript;
                }
            }

            // Show the interim transcript in the search bar for live feedback
            searchInput.value = finalTranscript || interimTranscript;

            // If we have a final, finalized transcript, submit the form
            if (finalTranscript) {
                searchInput.value = finalTranscript.trim();
                searchForm.submit();
            }
        };

        // Handle recognition errors
        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            // Ensure the click listener is removed on error as well
            document.removeEventListener('click', stopRecognitionOnClick);
            // e.g., micBtn.classList.remove('is-listening');
        };

    } else {
        // If not supported, hide the mic button
        micBtn.style.display = 'none';
        console.log('Speech recognition not supported in this browser.');
    }
});