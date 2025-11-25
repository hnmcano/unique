import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';


function App() {
  return (
    <Router>
        <main>
          <Routes>
            // rotas de paginas do site, sendo HomePage a primeira, caminho: /src/pages
            <Route path='/' element={<HomePage />} />
          </Routes>
        </main>
    </Router>
  );
}
export default App;
