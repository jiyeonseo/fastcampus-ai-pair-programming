'use client';
import { useEffect, useState } from 'react';
import { ProductList } from "@/components/product-list";

const Page = () => {
  const [products, setProducts] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch(`${be_url}/api/v1/products/?page=0&limit=6`);
      const newData = await res.json();
      setProducts(newData);
    }

    fetchData();
  }, []); // 컴포넌트가 마운트될 때 한 번만 실행
  
  if (!products) return <div>Loading...</div>;

  return (
    <div>
      <ProductList products={products} />
    </div>
  );
}

export default Page;