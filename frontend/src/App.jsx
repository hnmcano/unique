import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Inicio from './pages/Inicio';
import ListProdutosPedido from './components/Checkout/ListProdutosPedido';
import FormasPagPedido from './components/Checkout/FormasPagPedido';
import { CheckoutProvider } from './contexts/CheckoutContext';
import FormularioPedido from './components/Checkout/FormularioPedido';

function App() {
  return (
    <CheckoutProvider>
      <main>
        <Routes>
            // rotas de paginas do site, sendo HomePage a primeira, caminho: /src/pages
            <Route path='/' element={<Inicio />} /> 
            <Route path='/Checkout/Etapa1' element={<FormularioPedido />} />
            <Route path='/Checkout/Etapa2' element={<ListProdutosPedido />} />
            <Route path='/Checkout/Etapa3' element={<FormasPagPedido />} />
        </Routes>
      </main>
    </CheckoutProvider>
  );
}
export default App;
