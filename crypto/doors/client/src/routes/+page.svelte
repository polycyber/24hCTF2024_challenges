<script lang="ts">
	import { goto } from '$app/navigation';

	let username: String = '';
	let password: String = '';
	let loginAsGuestChecked: boolean = false;
	let errorMessage: String = '';

	async function onLoginClick() {
		if (!loginAsGuestChecked) {
			let res = await fetch('/api/login', {
				method: 'POST',
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ username: username, password: password })
			});

			if (res.status == 200) {
				goto('/admin');
			} else {
				errorMessage = 'Username or password invalid!';
			}
		} else {
			let res = await fetch('/api/login-guest', {
				method: 'POST',
				headers: {
					Accept: 'application/json',
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ username: username })
			});

			if (res.status == 200) {
				goto('/guest');
			} else {
				errorMessage = 'An error occured!';
			}
		}
	}
</script>

<div class="bg-white dark:bg-gray-700 p-8 rounded shadow-md w-96">
	<h2 class="text-2xl font-semibold mb-6">Prison Doors System Login</h2>

	<img alt="Prison Logo" src="polycyber-prison-logo.png"/>

	<form action="/login" method="POST">
		<div class="mb-4">
			<label for="username" class="block text-gray-700 dark:text-gray-300 text-sm font-bold mb-2"
				>Username</label
			>
			<input
				type="text"
				id="username"
				name="username"
				class="w-full px-3 py-2 border rounded dark:bg-gray-600"
				bind:value={username}
			/>
		</div>

		{#if !loginAsGuestChecked}
			<div class="mb-4">
				<label for="password" class="block text-gray-700 dark:text-gray-300 text-sm font-bold mb-2"
					>Password</label
				>
				<input
					type="password"
					id="password"
					name="password"
					class="w-full px-3 py-2 border rounded dark:bg-gray-600"
					bind:value={password}
				/>
			</div>
		{/if}
		<div class="mb-4 text-gray-700 dark:text-gray-300 text-sm">
			<input type="checkbox" bind:checked={loginAsGuestChecked} /> Login as guest
		</div>

		{#if errorMessage}
			<div class="mb-4 text-red-500">
				{errorMessage}
			</div>
		{/if}

		<button
			type="submit"
			class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 focus:outline-none focus:shadow-outline-blue"
			on:click|preventDefault={() => onLoginClick()}
		>
			Login
		</button>
	</form>
</div>
