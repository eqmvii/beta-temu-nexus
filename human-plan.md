# Goal

I need a self contained HTML file with vanilla JS (or jquery) JavaScript that mocks the homepage of migraine.com. Generally it's served by a Nuxt/Vue app that reads from an Elixir database. This HTML/JS/CSS mock will allow team members using Claude Code to create functional prototypes at the beginnig of the SDLC. 

The mock won't connect to ANY 3rd party APIs, it will be PURELY visual and lightly interactive. So lil json blobs or somethin for any data structures that might be helpful (users, comments, etc.)

The more this looks like our prod site, the more useful and impressive it will be. Pay attentino to details. 

# Specifics

Homepage mock: https://migraine.com/ (you can access this!)

Sample image of prod site in @temu-nexus/examples/

You have access to the Vue code that generates these pages in @nexus3/ - it is a Vue app that talks to an Elixir backend. You can reference that for things you NEED (colors, icons, etc.) or to dial in the design, but it's more imporant that the mocks roughly look like the pages and roughly behave like them than that they are pixel-perfect copies. 

# Initial State Requirements

- Homepage loads, has a static carousel component

- Menus open, none of the links need to work.

- Clicking login, for now, should toggle the menu icon to a logged in state 

- The mock should have clear placeholder fake ad slots. If it's feasible, make them generated fake ads instead of just grey placeholders. 

- the poll and email signup buttons don't need to work now, but might later

# Constraints

All work should be done in the @temu-nexus directory. I am likely to copy this directory into a new git project for deployment to GitHub pages, design accordingly. 

# Ask Me

Do you need more examples, or a static HTML dump or something? Do you need puppeteer or some means of seeing the HTML you create and continuing to iterate? Is the large screenshot dump I gave you helpful? 

# Future State

We will make a second post.html for a single post page. It will re-use the header, menus, and footer. 