
/** @jsxImportSource @emotion/react */import { Fragment, useCallback, useContext } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Button, Heading, VStack } from "@chakra-ui/react"
import { EventLoopContext, StateContexts } from "/utils/context"
import "focus-visible/dist/focus-visible"
import { Event } from "/utils/state"
import NextHead from "next/head"



export function Heading_c1e25984c026ed6f1095791c0cefa20c () {
  const state__estado = useContext(StateContexts.state__estado)


  return (
    <Heading sx={{"fontSize": "2em"}}>
  {state__estado.datos.at(2)}
</Heading>
  )
}

export function Button_66f794a55570b0dbcd90b503c4328dd2 () {
  const [addEvents, connectError] = useContext(EventLoopContext);

  const on_click_ccc29a67899752a245f9e08a422ed9a9 = useCallback((_e) => addEvents([Event("state.estado.refrescar", {})], (_e), {}), [addEvents, Event])

  return (
    <Button onClick={on_click_ccc29a67899752a245f9e08a422ed9a9}>
  {`Click Me!`}
</Button>
  )
}

export function Heading_ab4bdd18dafa8284555066b7c623fedf () {
  const state__estado = useContext(StateContexts.state__estado)


  return (
    <Heading sx={{"fontSize": "2em"}}>
  {state__estado.datos.at(1)}
</Heading>
  )
}

export function Heading_2731dd1c1eed5f6ddf9803ff0ec72a5c () {
  const state__estado = useContext(StateContexts.state__estado)


  return (
    <Heading sx={{"fontSize": "2em"}}>
  {state__estado.datos.at(0)}
</Heading>
  )
}

export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <VStack>
  <Heading_2731dd1c1eed5f6ddf9803ff0ec72a5c/>
  <Heading_ab4bdd18dafa8284555066b7c623fedf/>
  <Heading_c1e25984c026ed6f1095791c0cefa20c/>
  <Button_66f794a55570b0dbcd90b503c4328dd2/>
</VStack>
  <NextHead>
  <title>
  {`Reflex App`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
