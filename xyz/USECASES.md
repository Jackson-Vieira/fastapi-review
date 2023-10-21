# USE CASES

## Categoria

- add categoria
{
    name,
    slug
}

- listar categoria 
{
   id,
   name,
   slug 
}

- deletar categoria
{
    id
}

## Produtos

- adicionar produto
{
    name,
    slug,
    price,
    stock,
    category_slug
}

- atualizar produto
{
    name,
    slug,
    price,
    stock
}

- deletar produto
{
    id
}

- listar produtos
[produto -> categoria]

- filtrar produtos by `name` and `slug`
[]