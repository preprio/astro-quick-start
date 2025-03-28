# Astro Quick Start
The Astro quick start project launches a blog app with content from Prepr.

Check out the [Stackblitz demo](https://stackblitz.com/edit/astro-quick-start) for zero installation.

## Setup

Make sure to install the dependencies:

```bash
# yarn
yarn install

# npm
npm install

# pnpm
pnpm install --shamefully-hoist
```

## Add the environment file
Copy the .env.example file in this directory to .env (which will be ignored by Git) by running the following command:
```bash
cp .env.example .env
```

## Update the environment file
In the .env file replace `<YOUR-PREPR-API-URL>` with the Prepr access token from your environment with demo content.

## Development Server

Start the development server on http://localhost:4321

```bash
npm run dev
```

## Production

Build the application for production:

```bash
npm run build
```

Locally preview production build:

```bash
npm run preview
```

Check out the [deployment documentation](https://docs.astro.build/en/guides/deploy/) for more information.

## The end result

![blog site end result](https://assets-site.prepr.io//5oz8w28ybxje-screenshot-2023-05-10-at-111353.png)
