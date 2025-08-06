// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {

    // Get references to the theme toggle button and icons
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    // Function to apply the correct theme on page load
    const applyTheme = () => {
        // Check for a saved theme in localStorage or user's OS preference
        if (localStorage.getItem('color-theme') === 'dark' || 
           (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            // Apply dark theme
            document.documentElement.classList.add('dark');
            themeToggleLightIcon.classList.remove('hidden');
            themeToggleDarkIcon.classList.add('hidden');
        } else {
            // Apply light theme
            document.documentElement.classList.remove('dark');
            themeToggleDarkIcon.classList.remove('hidden');
            themeToggleLightIcon.classList.add('hidden');
        }
    };

    // Apply the theme when the page loads
    applyTheme();

    // Add a click event listener to the theme toggle button
    themeToggleBtn.addEventListener('click', () => {
        // Toggle the visibility of the sun and moon icons
        themeToggleDarkIcon.classList.toggle('hidden');
        themeToggleLightIcon.classList.toggle('hidden');

        // Check if a theme is already saved in localStorage
        if (localStorage.getItem('color-theme')) {
            // If the current theme is light, switch to dark
            if (localStorage.getItem('color-theme') === 'light') {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                // If the current theme is dark, switch to light
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            }
        // If no theme is saved in localStorage
        } else {
            // If the HTML element has the 'dark' class, switch to light
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                // If the HTML element does not have the 'dark' class, switch to dark
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        }
    });
});
