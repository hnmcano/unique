import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import DataFinalizacao from './pages/Finalizacao';

function App() {
  return (
      <main>
        <Routes>
            // rotas de paginas do site, sendo HomePage a primeira, caminho: /src/pages
            <Route path='/' element={<HomePage />} /> 
            <Route path='/conclusao' element={<DataFinalizacao />} />
        </Routes>
      </main>
  );
}
export default App;
