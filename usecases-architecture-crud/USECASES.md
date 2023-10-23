# USE CASES

## Categoria

- add categoria [X]
{
    name,
    slug
}

- listar categorias [X]
{
   id,
   name,
   slug 
}

- deletar categoria [X]
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