<template>
  <div class="chart-swap" :style="{ width }">
    <img :src="light" class="chart-img chart-img-light" :alt="alt" />
    <img :src="dark" class="chart-img chart-img-dark" :alt="alt" />
  </div>
</template>

<script setup>
// Renders the light and dark variants of one generated figure and lets CSS show
// whichever matches the current Slidev colour scheme. The deck is presented in
// dark mode, so this is not cosmetic: the light variant's dark ink is invisible
// on a dark slide. Both files come from scripts/make_charts.py.
const props = defineProps({
  name: { type: String, required: true },
  width: { type: String, default: '100%' },
  alt: { type: String, default: '' },
})

// The path has to be base-aware. Slidev serves each deck under its own
// sub-path in the workspace build (`/fdusc-ai-lecture/<deck>/`), so a
// root-absolute `/charts/x.svg` resolves to the site root and 404s — which is
// exactly what happened on the deployed site. BASE_URL is the deck's own base.
const base = import.meta.env.BASE_URL || '/'
const light = `${base}charts/${props.name}.svg`
const dark = `${base}charts/${props.name}-dark.svg`

</script>
