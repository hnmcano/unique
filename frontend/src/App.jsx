import { BrowserRouter as Router, Routes, Route, Form } from 'react-router-dom';
import Inicio from './pages/Inicio';
import "leaflet/dist/leaflet.css";
import ListProdutosPedido from './components/Checkout/ListProdutosPedido';
import FormasPagPedido from './components/Checkout/FormasPagPedido';
import { CheckoutProvider } from './contexts/CheckoutContext';
import { CarrinhoProvider } from './contexts/CarrinhoContext';
import { StatusProvider } from './contexts/StatusContext';
import { CardProvider } from './contexts/HorariosContext';
import { EstabelecimentoProvider } from './contexts/EstabelecimentoContext';
import FormularioCliente from './components/Checkout/FormularioCliente';
import FormularioEntrega from './components/Checkout/FormularioEntrega';
import AcompanhamentoPedido from './components/Status/AcompanhamentoPedido';

function App() {
  return (
    <EstabelecimentoProvider>
      <CarrinhoProvider>
        <CheckoutProvider>
          <StatusProvider>
            <CardProvider>
              <main>
                <Routes>
                    // rotas de paginas do site, sendo HomePage a primeira, caminho: /src/pages
                    <Route path='/' element={<Inicio />} /> 
                    <Route path='/Checkout/Etapa1' element={<FormularioCliente />}/>
                    <Route path='/Checkout/Etapa2' element={<FormularioEntrega />}/>
                    <Route path='/Checkout/Etapa3' element={<ListProdutosPedido />}/>
                    <Route path='/Checkout/Etapa4' element={<FormasPagPedido />}/>
                    <Route path='/Status/Pedido/:id_pedido' element= {<AcompanhamentoPedido />}/>
                </Routes>
              </main>
            </CardProvider>
          </StatusProvider>
        </CheckoutProvider>
      </CarrinhoProvider>
    </EstabelecimentoProvider>
  );
}
export default App;
