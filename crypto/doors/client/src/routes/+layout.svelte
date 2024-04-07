<script>
	import { onMount } from 'svelte';
	import '../app.css';

	onMount(() => {
		loadTheme();
	});

	function toggleDarkMode() {
		if ('theme' in localStorage) {
			if (localStorage.theme == 'light') {
				localStorage.theme = 'dark';
			} else {
				localStorage.theme = 'light';
			}
		} else {
			if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
				localStorage.theme = 'dark';
			} else {
				localStorage.theme = 'light';
			}
		}

		loadTheme();
	}

	function loadTheme() {
		if (
			localStorage.theme === 'dark' ||
			(!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
		) {
			document.documentElement.classList.add('dark');
		} else {
			document.documentElement.classList.remove('dark');
		}
	}
</script>

<button
	id="dark-mode-toggle"
	class="absolute top-2 right-2 bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 px-4 py-2 rounded-full focus:outline-none"
	on:click={() => toggleDarkMode()}
>
	Toggle Dark Mode
</button>
<slot />
