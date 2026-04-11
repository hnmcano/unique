// App.jsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { ContextProvider } from './Context/ContextData'
import { Header } from './components/Header'
import { Hero } from './components/Hero'
import { Features } from './components/Features'
import { Stats } from './components/Stats'
import { Testimonials } from './components/Testimonials'
import { Pricing } from './components/Pricing'
import { CTA } from './components/cta'
import { Footer } from './components/Footer'
import Register from './pages/Register'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import PrivateRoute from "./components/PrivateRoute";

function HomePage() {
  return (
    <>
      <Header />
      <main >
        <Hero />
        <Stats />
        <Features />
        <Testimonials />
        <Pricing />
        <CTA />
      </main>
      <Footer />
    </>
  )
}

function App() {
  return (
    <ContextProvider>
    
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
            <Route path="/dashboard" element={
                <PrivateRoute >
                  <Dashboard />
                </PrivateRoute>
              } 
            />
        </Routes>
      </Router>
    </ContextProvider>
  )
}

export default App