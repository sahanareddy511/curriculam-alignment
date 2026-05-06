document.getElementById('analyzeForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const loadingDiv = document.getElementById('loading');
    const resultsDiv = document.getElementById('results');
    const analyzeBtn = document.getElementById('analyzeBtn');

    // Show loading, hide results
    loadingDiv.classList.remove('hidden');
    resultsDiv.classList.add('hidden');
    analyzeBtn.disabled = true;

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            displayResults(data);
        } else {
            alert('Error: ' + (data.error || 'Something went wrong'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to connect to the server.');
    } finally {
        loadingDiv.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
});

function displayResults(data) {
    const resultsDiv = document.getElementById('results');
    
    // 1. Match Score
    document.getElementById('matchPercent').textContent = data.match_percent + '%';

    // 2. Lists
    const missingList = document.getElementById('missingSkillsList');
    const resumeList = document.getElementById('resumeSkillsList');
    
    missingList.innerHTML = '';
    resumeList.innerHTML = '';

    if (data.missing_skills.length === 0) {
        missingList.innerHTML = '<li>None! You are a perfect match.</li>';
    } else {
        data.missing_skills.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            missingList.appendChild(li);
        });
    }

    if (data.resume_skills.length === 0) {
        resumeList.innerHTML = '<li>No relevant skills found.</li>';
    } else {
        data.resume_skills.forEach(skill => {
            const li = document.createElement('li');
            li.textContent = skill;
            resumeList.appendChild(li);
        });
    }

    // 3. Roadmap
    const roadmapContainer = document.getElementById('roadmapContainer');
    roadmapContainer.innerHTML = '';

    // Convert roadmap object to array and sort by week
    const roadmapEntries = Object.entries(data.roadmap).sort((a, b) => {
        // Simple sort by Week number (assuming format "Week X")
        const weekA = parseInt(a[0].replace('Week ', ''));
        const weekB = parseInt(b[0].replace('Week ', ''));
        return weekA - weekB;
    });

    roadmapEntries.forEach(([week, plan]) => {
        const div = document.createElement('div');
        div.className = 'roadmap-item';
        div.innerHTML = `<span class="roadmap-week">${week}</span> ${plan}`;
        roadmapContainer.appendChild(div);
    });

    // Show results
    resultsDiv.classList.remove('hidden');
}