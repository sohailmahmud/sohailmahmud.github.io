import re

with open('src/pages/index.astro', 'r') as f:
    html = f.read()

start_marker = '<div class="grid lg:grid-cols-12 gap-12 lg:gap-8 items-center">'
end_marker = '<!-- Stats Section (4 Metric Cards) -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers")
    exit(1)

new_hero = """<div class="grid lg:grid-cols-12 gap-12 lg:gap-8 items-center">
      <!-- Left Column: Text & Tech Stack -->
      <div class="lg:col-span-7 flex flex-col justify-center">
        <!-- Badge -->
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-50 border border-emerald-100 text-emerald-600 text-xs font-semibold mb-6 sm:mb-8 self-start shadow-sm">
          <span class="relative flex h-2 w-2">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          Available for new opportunities
        </div>

        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-zinc-900 tracking-tight leading-[1.1] mb-6">
          Senior Fullstack<br/>Mobile Engineer &<br/>
          <span class="text-emerald-500">Tech Leader.</span>
        </h1>
        
        <p class="text-base sm:text-lg text-zinc-600 mb-8 sm:mb-10 max-w-xl leading-relaxed">
          I build scalable mobile apps, robust backend systems, and cloud-native solutions that solve real business problems and create impactful user experiences.
        </p>

        <div class="flex flex-col sm:flex-row items-start sm:items-center gap-4 mb-10 sm:mb-12">
          <a 
            href="mailto:hello@sohailmahmud.com" 
            class="bg-zinc-900 hover:bg-zinc-800 text-white font-medium text-sm px-6 py-3.5 rounded-xl inline-flex items-center gap-2 transition-all shadow-sm hover:no-underline group"
          >
            Let's Work Together 
            <span class="group-hover:translate-x-1 transition-transform">&rarr;</span>
          </a>
          <a 
            href="#work" 
            class="bg-white hover:bg-zinc-50 text-zinc-900 border border-zinc-200 font-medium text-sm px-6 py-3.5 rounded-xl inline-flex items-center gap-2 transition-all shadow-sm hover:no-underline"
          >
            View My Work
            <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4 text-zinc-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="7" height="7"></rect>
              <rect x="14" y="3" width="7" height="7"></rect>
              <rect x="14" y="14" width="7" height="7"></rect>
              <rect x="3" y="14" width="7" height="7"></rect>
            </svg>
          </a>
        </div>

        <!-- Tech Stack Logos -->
        <div class="flex flex-wrap items-center gap-x-6 gap-y-4 text-xs font-medium text-zinc-500">
          
          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet"><path fill="#f05138" d="M110.15 210.02c11.08 6.54 26.68 12.01 44.53 13.91 10.36 1.11 20.89 1.16 31.02.13-10.97-15.03-31.25-33.15-54.89-42.34-11.23-4.36-23.77-7.46-37.49-9.15 13.78-4.14 27.24-9.3 39.81-15.65-27.13 6.94-55.51 7.22-79.62 1.4-1.29-.31-2.58-.65-3.83-1.02a159.27 159.27 0 0 1-28.53-11.53c4.13 32.74 36.43 65.59 89.01 64.25ZM256 18.06c-8.91-4.73-35.34-14.86-77.58-9.14-19.1 2.58-39.26 9.39-58.4 20.2-12.72 7.18-24.8 15.91-35.25 25.59 2.51-6.14 5.37-12.08 8.44-17.78C53.79 66.86 17.5 106.63 1.09 154.51c36.63-22.14 83.25-37.75 130.64-32.96 46.52 4.71 85.39 28.58 109.84 62.77C220.5 134.42 165 91.56 103.53 82.26c36.75 3.03 71.05 15.22 101.44 33.34C244.64 81.33 255.45 37.1 256 18.06Z"/></svg>
            <span>Swift</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMin meet"><path fill="#f88909" d="M256 256H0V0h256l-128 128z"/><path fill="#0095d5" d="M0 0l128 128L0 256z"/></svg>
            <span>Kotlin</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><path fill="#3eb6ea" d="M12.981 61.27 63.81 10.441l17.842-17.842h-35.73L12.981 25.54z"/><path fill="#02539a" d="m42.502 90.793-11.666 11.68 11.666 11.68h35.73l-29.544-29.544z"/><path fill="#3eb6ea" d="m63.81 112.56-12.062-12.046 29.544-29.544H117.02z"/><path fill="#54c5f8" d="M63.81 70.97 12.981 20.14h35.73L99.54 70.97z"/></svg>
            <span>Flutter</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" viewBox="0 0 256 256" xmlns="http://www.w3.org/2000/svg"><path fill="#512bd4" d="M192.68 18.825a39.814 39.814 0 0 0-33.15 17.51l.056-.095c-30.828-17.65-68.535-17.61-99.363 0a113.88 113.88 0 0 0-49.721 86.1c0 62.775 51.05 113.824 113.825 113.824s113.824-51.05 113.824-113.825a113.25 113.25 0 0 0-12.28-51.528 39.851 39.851 0 1 0-33.191-51.986zm-20.91 165.738c-8.91 10.493-21.84 15.65-38.647 15.65-27.126 0-46.06-16.143-46.06-44.622 0-25.795 18.256-43.5 45.47-43.5 16.48 0 28.777 4.975 37.106 14.739.736.87 1.258 2.38.716 3.66L164.218 139.7c-.504 1.144-1.879 1.415-3.04 1.104-5.323-2.38-12.518-4.996-22.186-4.996-13.615 0-22.957 8.324-22.957 20.871 0 11.233 8.36 19.336 21.6 19.336 11.42 0 19.014-3.177 24.316-6.195.968-.543 2.188-.136 2.653.85l6.541 12.025a1.864 1.864 0 0 1 .625 1.87zm-79.914 14.07h-21.72a2.31 2.31 0 0 1-2.323-2.324V112.541c0-1.28.987-2.323 2.323-2.323h21.72a2.32 2.32 0 0 1 2.324 2.323v83.743c0 1.28-1.045 2.325-2.324 2.325z"/></svg>
            <span>.NET Core</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg"><path fill="#dc291a" d="M125.8 44.912c-5.744-8.832-15.01-16.143-26.68-20.91-11.442-4.664-24.168-6.938-36.568-6.527-14.739.485-28.718 4.414-40.237 11.233-10.743 6.388-18.784 14.935-21.576 25.132 2.457-11.432 10.336-20.9 21.033-27.1 11.52-6.685 25.568-10.457 40.355-10.825 12.35-.31 25.045 1.902 36.425 6.452 11.66 4.673 20.914 11.906 26.641 20.672zM4.148 57.067c2.404-5.3 6.963-9.54 12.799-11.9 6.273-2.545 13.578-3.415 20.67-2.46l.87.116.793.136c1.644.29 3.251.658 4.819 1.103v15.03c-1.567-.348-3.154-.62-4.757-.792l-.772-.098-.792-.058c-6.223-.33-12.785.736-18.067 2.946-4.57 1.9-8.497 4.956-11.332 8.76l18.528 15.093v15.115C13.258 87.03 3.511 72.88 4.15 57.065ZM61.85 43.149c-4.432.063-9.664 1.052-13.621 3.832-1.223.883-1.012 2.062.336 1.894 4.508-.547 14.44-1.726 16.21.547 1.77 2.23-1.976 11.62-3.663 15.79-.504 1.26.59 1.769 1.726.8 7.41-6.231 9.348-19.242 7.832-21.137-.757-.925-4.388-1.79-8.82-1.726zM1.63 75.859c-.927.116-1.347 1.236-.368 2.121 16.508 14.902 38.359 23.872 62.613 23.872 17.305 0 37.43-5.43 51.281-15.66 2.273-1.688.297-4.254-2.02-3.204-15.534 6.57-32.421 9.77-47.788 9.77-22.778 0-44.8-6.273-62.653-16.633-.39-.231-.755-.304-1.064-.266z"/></svg>
            <span>MS SQL</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><path fill="#ffa000" d="M17.474 103.276 33.229 2.462a2.91 2.91 0 0 1 5.44-.924l16.294 30.39 6.494-12.366a2.91 2.91 0 0 1 5.15 0l43.97 83.714H17.474Z"/><path fill="#f57c00" d="M71.903 64.005 54.955 31.913l-37.481 71.363Z"/><path fill="#ffca28" d="M110.577 103.276 98.51 28.604a2.913 2.913 0 0 0-1.984-2.286 2.906 2.906 0 0 0-2.94.714l-76.112 76.243 42.115 23.618a8.728 8.728 0 0 0 8.51 0l42.478-23.618Z"/><path fill="#fff" fill-opacity=".2" d="M98.51 28.604a2.913 2.913 0 0 0-1.984-2.286 2.906 2.906 0 0 0-2.94.713L78.479 42.178 66.6 19.562a2.91 2.91 0 0 0-5.15 0l-6.494 12.365L38.662 1.538A2.91 2.91 0 0 0 35.605.044a2.907 2.907 0 0 0-2.384 2.425L17.474 103.276h-.051l.05.058.415.204 75.676-75.764a2.91 2.91 0 0 1 4.932 1.571l11.965 74.003.116-.073L98.51 28.603Zm-80.898 74.534L33.228 3.182A2.91 2.91 0 0 1 35.613.756a2.911 2.911 0 0 1 3.057 1.495l16.292 30.39 6.495-12.366a2.91 2.91 0 0 1 5.15 0L78.245 42.41 17.61 103.138Z"/><path fill="#a52714" d="M68.099 126.18a8.728 8.728 0 0 1-8.51 0l-42.015-23.55-.102.647 42.115 23.61a8.728 8.728 0 0 0 8.51 0l42.48-23.61-.11-.67-42.37 23.575z" opacity=".2"/></svg>
            <span>Firebase</span>
          </div>

          <div class="flex items-center gap-1.5 hover:text-zinc-900 transition-colors">
            <svg class="w-3.5 h-3.5" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg"><path fill="#f90" d="M84.28 73.01c-6.84 3.73-16.71 6.84-27.59 6.84-21.72 0-38.41-8.5-51.27-22.18-.73-.77-.42-1.89.58-1.9 9.38-.13 21.05 1.15 29.83 5.48 1.48.73 1.18 2.66-.27 3.03-9.58 2.45-19.14 1.83-26.68.74-1.3-.18-1.92 1.35-.91 2.22 8.42 7.2 21.82 14.1 39.52 14.1 11.23 0 20.89-2.78 28.52-5.46 1.47-.52 2.62 1.25 1.28 2.11a136.21 136.21 0 0 1-28.84 10.98c-8.91 1.94-18.73 2.1-25.59 1.49-1.33-.12-1.95 1.45-.89 2.25 10.23 7.74 25.1 13.9 44.13 13.9 14.2 0 26.63-3.66 35.12-7.55 1.76-.81 2.82 1.5 1.15 2.5a91.31 91.31 0 0 1-29.35 11.26c-11.46 2.23-22.95 2.12-30.82 1.44-1.39-.12-1.93 1.56-.76 2.3 11.75 7.42 27.67 12.3 46.54 12.3 16.5 0 31.42-4.14 42.27-8.98 1.94-.86 3.06 1.7 1.14 2.8-11.59 6.64-28.78 11.43-46.77 11.43-20.9 0-38.71-5.74-51.52-14.16-1.52-.99-.68-3.03.95-2.61 8.8 2.26 18.74 3.05 28.77 2.47 13.56-.79 26.11-4.14 36.63-8.8 1.87-.83.6-3.37-1.18-2.48z"/><path fill="#232f3e" d="M102.57 28.32c-.17 0-.31.02-.45.06l-9.14 2.57c-.2.06-.32.26-.26.46l4.63 16.48c.06.2.26.32.46.26l9.14-2.57c.2-.06.32-.26.26-.46L102.83 28.5a.36.36 0 0 0-.26-.18zm-4.32 6.8 5.76-1.62-1.28 4.57-5.76 1.62 1.28-4.57zM86.84 32.74l-6.22 1.75c-.2.06-.32.26-.26.46l2.18 7.76c.06.2.26.32.46.26l6.22-1.75c.2-.06.32-.26.26-.46l-2.18-7.76a.36.36 0 0 0-.26-.18zm-2.02 5.59 2.56-.72-.57 2.03-2.56.72.57-2.03zM67.12 38.29l-11.96 3.36c-.2.06-.32.26-.26.46l1.24 4.41c.06.2.26.32.46.26l11.96-3.36c.2-.06.32-.26.26-.46l-1.24-4.41a.36.36 0 0 0-.26-.18zm-2.99 4.31 8.3-2.33-.35 1.24-8.3 2.33.35-1.24zM54.78 41.76l-14.88 4.18c-.2.06-.32.26-.26.46l.73 2.6c.06.2.26.32.46.26l14.88-4.18c.2-.06.32-.26.26-.46l-.73-2.6a.36.36 0 0 0-.26-.18zm-2.47 3.32 11.23-3.15-.21.75-11.23 3.15.21-.75z"/></svg>
            <span>AWS</span>
          </div>

          <span class="text-zinc-400 text-xs font-normal">••• More</span>
        </div>
      </div>

      <!-- Right Column: Hero Visual & Floating Badge -->
      <div class="lg:col-span-5 flex justify-center lg:justify-end relative pb-10 lg:pb-8">
        <!-- Dotted pattern backdrop & image container -->
        <div class="relative w-full max-w-[340px] sm:max-w-[380px]">
          <div class="absolute -top-6 -right-6 w-48 h-48 bg-emerald-100/40 rounded-full blur-2xl -z-10"></div>
          <div class="relative rounded-3xl overflow-hidden shadow-xl border border-zinc-200/60 bg-white">
            <img 
              src="/images/headshot.jpg" 
              alt="Sohail Mahmud - Senior Fullstack Mobile Engineer & Tech Leader" 
              class="w-full h-auto object-cover object-center"
            />
          </div>

          <!-- Floating Tech Leader Card Overlay (Bottom-Center) -->
          <div class="absolute -bottom-6 left-1/2 -translate-x-1/2 w-[92%] sm:w-auto min-w-[280px] sm:min-w-[300px] bg-white/95 backdrop-blur-md p-3.5 sm:p-4 rounded-2xl border border-zinc-200/80 shadow-xl flex items-center gap-3.5 z-10">
            <div class="w-10 h-10 rounded-xl bg-emerald-50 flex items-center justify-center shrink-0 text-emerald-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                <circle cx="9" cy="7" r="4"></circle>
                <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
              </svg>
            </div>
            <div>
              <h4 class="font-bold text-xs sm:text-sm text-zinc-900 leading-tight">Tech Leader</h4>
              <p class="text-[10px] sm:text-xs text-zinc-500 font-medium mt-0.5">Mentor • Architect • Problem Solver</p>
              <p class="text-[10px] text-zinc-600 font-normal mt-0.5">Turning ideas into scalable products</p>
            </div>
          </div>
        </div>
      </div>
    </div>
"""

new_html = html[:start_idx] + new_hero + html[end_idx:]

with open('src/pages/index.astro', 'w') as f:
    f.write(new_html)

