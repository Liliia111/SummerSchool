import React from 'react';
import {render} from 'react-dom';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Button from '@material-ui/core/Button';

const App = () => (
<MuiThemeProvider>
    <Button variant="contained">
        Default
    </Button>
</MuiThemeProvider>
);

render(<App />, document.getElementById('app'));