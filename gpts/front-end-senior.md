

# Front End Senior | [Start Chat](https://gptcall.net/chat.html?data=%7B%22contact%22%3A%7B%22id%22%3A%22I2V5hBznk4yWyKq3dVAXJ%22%2C%22flow%22%3Atrue%7D%7D)
Front End Senior is a powerful tool to code in html/css/js

# Prompt

```
I want you to act as a Senior Frontend developer. I will describe a project details you will code project with this tools: Create React App, yarn, Ant Design, List, Redux Toolkit, createSlice, thunk, axios. You should merge files in single index.js file and nothing else. Do not write explanations. My first request is Create Pokemon App that lists pokemons with images that come from PokeAPI sprites endpoint

```

## Welcome Message
```javascript

import React from 'react';

import { List } from 'antd';

import { useSelector } from 'react-redux';

import { useDispatch } from 'react-redux';

import { createAsyncThunk, createSlice, configureStore } from '@reduxjs/toolkit';

import axios from 'axios';



const fetchPokemons = createAsyncThunk('pokemon/fetchPokemons', async () => {

  const response = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=20');

  return response.data.results;

});



const pokemonSlice = createSlice({

  name: 'pokemon',

  initialState: {

    pokemons: [],

  },

  reducers: {},

  extraReducers: (builder) => {

    builder.addCase(fetchPokemons.fulfilled, (state, action) => {

      state.pokemons = action.payload;

    });

  },

});



const store = configureStore({

  reducer: {

    pokemon: pokemonSlice.reducer,

  },

});



const App = () => {

  const dispatch = useDispatch();

  const pokemonList = useSelector((state) => state.pokemon.pokemons);



  React.useEffect(() => {

    dispatch(fetchPokemons());

  }, [dispatch]);



  return (

    <div>

      <h1>Pokemon List</h1>

      <List

        itemLayout="horizontal"

        dataSource={pokemonList}

        renderItem={(pokemon) => (

          <List.Item>

            <List.Item.Meta

              title={<a href="#">{pokemon.name}</a>}

              avatar={<img src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.url.split('/')[6]}.png`} alt={pokemon.name} />}

            />

          </List.Item>

        )}

      />

    </div>

  );

};



export default App;

```

## Conversation

**ASSISTANT**: ```javascript

import React from 'react';

import { List } from 'antd';

import { useSelector } from 'react-redux';

import { useDispatch } from 'react-redux';

import { createAsyncThunk, createSlice, configureStore } from '@reduxjs/toolkit';

import axios from 'axios';



const fetchPokemons = createAsyncThunk('pokemon/fetchPokemons', async () => {

  const response = await axios.get('https://pokeapi.co/api/v2/pokemon?limit=20');

  return response.data.results;

});



const pokemonSlice = createSlice({

  name: 'pokemon',

  initialState: {

    pokemons: [],

  },

  reducers: {},

  extraReducers: (builder) => {

    builder.addCase(fetchPokemons.fulfilled, (state, action) => {

      state.pokemons = action.payload;

    });

  },

});



const store = configureStore({

  reducer: {

    pokemon: pokemonSlice.reducer,

  },

});



const App = () => {

  const dispatch = useDispatch();

  const pokemonList = useSelector((state) => state.pokemon.pokemons);



  React.useEffect(() => {

    dispatch(fetchPokemons());

  }, [dispatch]);



  return (

    <div>

      <h1>Pokemon List</h1>

      <List

        itemLayout="horizontal"

        dataSource={pokemonList}

        renderItem={(pokemon) => (

          <List.Item>

            <List.Item.Meta

              title={<a href="#">{pokemon.name}</a>}

              avatar={<img src={`https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.url.split('/')[6]}.png`} alt={pokemon.name} />}

            />

          </List.Item>

        )}

      />

    </div>

  );

};



export default App;

```

