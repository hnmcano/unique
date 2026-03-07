import type { Metadata } from 'next'
import { Geist, Geist_Mono } from 'next/font/google'
import React from 'react'
import { Analytics } from '@vercel/analytics/react';
import './globals.css'

const _geist = Geist({ subsets: ["latin"] });
const _geistMono = Geist_Mono({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: 'UNIQUE - PDV e Delivery | Solução Completa para seu Negócio',
  description: 'Transforme suas vendas com UNIQUE. Solução completa de PDV e Delivery com gestão eficiente e entrega ágil.',
  generator: 'v0.app',
  icons: {
    icon: [
      {
        url: '/icon-light-32x32.png',
        media: '(prefers-color-scheme: light)',
      },
      {
        url: '/icon-dark-32x32.png',
        media: '(prefers-color-scheme: dark)',
      },
      {
        url: '/icon.svg',
        type: 'image/svg+xml',
      },
    ],
    apple: '/apple-icon.png',
  },
}

export default function RootLayout({
    children,
  }: Readonly<{
    children: React.ReactNode
  }>) {
    return (
        <>
          <html lang="en">
            <body className="font-sans antialiased">
              {children}
              <Analytics />
            </body>
          </html>
      </>
    )
}
