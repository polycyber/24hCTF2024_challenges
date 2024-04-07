<script lang="ts">
	import { onMount } from 'svelte';

	let content: String = '';
	onMount(async () => {
		let res = await fetch('/api/public');

		if (res.status == 200) {
			content = await res.text();
		} else {
			content = "You don't have the permission to view this!";
		}
	});
</script>

<div>
	{content}
</div>
