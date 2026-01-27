import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Inicio from './pages/Inicio';
import Pedido from './pages/Pedido';

function App() {
  return (
      <main>
        <Routes>
            // rotas de paginas do site, sendo HomePage a primeira, caminho: /src/pages
            <Route path='/' element={<Inicio />} /> 
            <Route path='/conclusao' element={<Pedido />} />
        </Routes>
      </main>
  );
}
export default App;
