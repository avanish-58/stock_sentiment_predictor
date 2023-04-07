const searchInput = document.getElementById('search');
const suggestionsList = document.getElementById('suggestions');

const countries = ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Chile', 'Colombia', 'Peru', 'Ecuador'];

function displaySuggestions(event) {
  const searchText = event.target.value.toLowerCase();
  const suggestions = countries.filter(country => country.toLowerCase().startsWith(searchText));
  suggestionsList.innerHTML = '';
  suggestions.forEach(suggestion => {
    const li = document.createElement('li');
    li.textContent = suggestion;
    suggestionsList.appendChild(li);
  });
}

searchInput.addEventListener('input', displaySuggestions);